# dashboard/app.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import pandas as pd
from config.load_config import load_config

def load_data():
    config = load_config()
    return pd.read_json(config['output_file'], lines=True)

def render_dashboard():
    st.set_page_config(page_title="SmartFlow Traffic Monitor", layout="wide")
    st.title("📊 SmartFlow: Website Traffic Anomaly Dashboard")

    df = load_data()

    st.subheader("📈 Traffic Over Time")
    st.line_chart(data=df, x='timestamp', y='value', use_container_width=True)

    st.subheader("🚨 Detected Anomalies")
    anomalies = df[df['is_anomaly'] == True]

    if not anomalies.empty:
        st.table(anomalies[['timestamp', 'value', 'anomaly_score']])
    else:
        st.success("✅ No anomalies detected.")

    st.sidebar.markdown("### 🔍 Stats")
    st.sidebar.metric("Total Records", len(df))
    st.sidebar.metric("Anomalies", len(anomalies))

if __name__ == "__main__":
    render_dashboard()
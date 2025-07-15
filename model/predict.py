# model/predict.py

import pandas as pd
import joblib
import numpy as np
from config.load_config import load_config
from alerts.send_alert import send_email_alert

def run_inference():
    config = load_config()

    # Load preprocessed data and model
    df = pd.read_csv(config['processed_data_file'])
    clf = joblib.load(config['model_file'])

    # Run model inference
    X = df[['value_scaled']]
    df['anomaly_score'] = clf.decision_function(X)
    df['is_anomaly'] = clf.predict(X) == -1

    # Apply business rule if enabled
    if config.get('hybrid_mode', False):
        median_traffic = np.median(df['value'])
        threshold = config.get('anomaly_multiplier', 2.5) * median_traffic

        df['is_anomaly'] = df.apply(
            lambda row: True if (not row['is_anomaly'] and row['value'] > threshold) else row['is_anomaly'],
            axis=1
        )

    # Save output to JSON
    df[['timestamp', 'value', 'anomaly_score', 'is_anomaly']].to_json(
        config['output_file'], orient='records', lines=True
    )

    # Alert if anomalies detected
    if config.get('enable_alerts', False):
        anomalies = df[df['is_anomaly'] == True]
        if not anomalies.empty:
            alert_body = f"🚨 {len(anomalies)} anomaly(ies) detected.\n\n{anomalies[['timestamp','value']].to_string()}"
            send_email_alert(subject="SmartFlow Alert: Website Traffic Anomalies", body=alert_body)

    print(f"✅ Inference complete using hybrid mode: {config.get('hybrid_mode', False)}")
    print(f"📁 Results saved to {config['output_file']}")

if __name__ == "__main__":
    run_inference()
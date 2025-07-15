# 🧠 SmartFlow: AI-Powered Website Traffic Anomaly Detection Pipeline
## 🚀 Overview
SmartFlow is a modular, configurable data pipeline designed to detect abnormal spikes in website traffic using a hybrid model: machine learning + business rules. Built with Python, Streamlit, and Airflow-ready ingestion logic, this project demonstrates how intelligent automation can transform time-series data into actionable insights.
---
## 🏗️ Architecture
┌──────────────┐ │ Traffic CSV │ └─────┬────────┘ ▼ ┌─────────────────────────┐ │ Ingestion Layer │ │ (Airflow DAG / Manual) │ └────────┬────────────────┘ ▼ ┌─────────────────────────┐ │ Preprocessing (Pandas) │ └────────┬────────────────┘ ▼ ┌──────────────────────────────┐ │ Hybrid Detection Engine │ │ - Isolation Forest (ML) │ │ - Business Rule Override │ └────────┬─────────────────────┘ ▼ ┌─────────────────────────┐ │ Alert Engine (Email) │ └────────┬────────────────┘ ▼ ┌─────────────────────────┐ │ Streamlit Dashboard │ └─────────────────────────┘
---
## 🔧 Technologies Used
| Tool           | Purpose                                   |
|----------------|--------------------------------------------|
| Python         | Core scripting and orchestration           |
| Pandas         | Data manipulation and time-series handling |
| Scikit-learn   | Isolation Forest model                     |
| PyYAML         | Config file parsing                        |
| Joblib         | Model persistence                         |
| Streamlit      | Dashboard visualization                    |
| SMTP (email)   | Sending alerts for detected anomalies      |
---
## 📁 Folder Structure
smartflow-ai-pipeline/
├── data/              ← Sample traffic logs
├── ingestion/         ← Ingestion logic (Airflow or manual)
├── preprocessing/     ← Clean & scale data
├── model/             ← Train & run anomaly detection
├── alerts/            ← Notification engine
├── dashboard/         ← Streamlit UI
├── config/            ← Pipeline config.yml
├── output/            ← Results (.json)
├── tests/             ← Unit tests
├── run_pipeline.py    ← End-to-end pipeline executor
├── requirements.txt   ← Dependencies
└── README.md          ← You're here!
---
## ⚙️ Setup Instructions
### 1. Clone the Repo
```bash
git clone https://github.com/anhonghu/smartflow-ai-pipeline.git
cd smartflow-ai-pipeline
### 2. Install Requirements
```bash
pip install -r requirements.txt
### 3. Run the Pipeline
```bash
python run_pipeline.py
### 4. Launch the Dashboard
```bash
streamlit run dashboard/app.py
---
## 🧪 Sample Output
{
  "timestamp": "2025-07-08T09:35:00Z",
  "value": 1600,
  "anomaly_score": -0.42,
  "is_anomaly": true
}
This shows a promotional traffic spike flagged as an anomaly.
---
## 🧠 Hybrid Detection Logic
Combines statistical modeling with domain expertise to improve anomaly detection.
### Model: Isolation Forest detects statistical outliers
### Business Rule Override: Flags any traffic ≥ 2.5× median value — ideal for campaign surges
---
## 🔔 Alerts Module
### Automatically sends email when traffic anomalies are detected
### Configurable SMTP settings via config.yml
### Easy extension to support Slack, Discord, SNS, or SMS
---
## 📈 Dashboard Features
### Line chart of web traffic over time
### Highlighted anomalies with score details
### Sidebar metrics on total records and anomaly count
---
## 📌 Requirements
pandas==2.2.2
scikit-learn==1.4.2
pyyaml==6.0.1
streamlit==1.34.0
joblib==1.4.2

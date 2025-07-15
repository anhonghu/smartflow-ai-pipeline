# ingestion/airflow_dag.py
# This Airflow DAG ingests data from a CSV file and saves it to a specified directory.
# It uses the PythonOperator to execute a Python function that reads the CSV file and writes it
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

def ingest_data():
    df = pd.read_csv('data/sample_input.csv')
    df.to_csv('preprocessing/raw_data.csv', index=False)

default_args = {
    'owner': 'anhong',
    'start_date': datetime(2025, 7, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='smartflow_ingestion_dag',
    default_args=default_args,
    schedule_interval='@hourly',
    catchup=False
) as dag:

    ingestion_task = PythonOperator(
        task_id='ingest_csv_data',
        python_callable=ingest_data
    )

    ingestion_task
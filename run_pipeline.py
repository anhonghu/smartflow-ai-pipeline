# run_pipeline.py

import sys
def try_import_ingest_data():
    try:
        from ingestion.airflow_dag import ingest_data
        return ingest_data
    except ImportError:
        print("⚠️  Airflow is not installed. Skipping data ingestion step.")
        return None
from preprocessing.clean_data import preprocess_data
from model.train_model import train_model
from model.predict import run_inference
from config.load_config import load_config

def main():
    config = load_config()
    print("\n🚀 SmartFlow AI Pipeline Starting...\n")

    try:
        print("📥 Step 1: Ingesting data")
        ingest_data = try_import_ingest_data()
        if ingest_data:
            ingest_data()
        else:
            print("Skipping ingestion step.")

        print("\n🧹 Step 2: Preprocessing data")
        preprocess_data()

        print("\n🧠 Step 3: Training model")
        train_model()

        print("\n🔍 Step 4: Running inference")
        run_inference()

        print("\n✅ Pipeline execution complete!")
    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
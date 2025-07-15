# model/train_model.py

import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
from config.load_config import load_config

def train_model():
    config = load_config()
    df = pd.read_csv(config['processed_data_file'])
    X = df[['value_scaled']]

    clf = IsolationForest(
        contamination=config['contamination'],
        random_state=config['random_state']
    )
    clf.fit(X)
    joblib.dump(clf, config['model_file'])
    print(f"✅ Model trained and saved to {config['model_file']}")

if __name__ == "__main__":
    train_model()
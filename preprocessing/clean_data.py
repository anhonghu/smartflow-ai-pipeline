# preprocessing/clean_data.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from config.load_config import load_config

def preprocess_data():
    config = load_config()

    input_path = config['raw_data_file']
    output_path = config['processed_data_file']

    # Load raw data
    df = pd.read_csv(input_path, parse_dates=['timestamp'])

    # Drop missing values
    df.dropna(inplace=True)

    # Sort by timestamp
    df.sort_values(by='timestamp', inplace=True)

    # Normalize using MinMaxScaler
    scaler = MinMaxScaler()
    df['value_scaled'] = scaler.fit_transform(df[['value']])

    # Save processed data
    df.to_csv(output_path, index=False)
    print(f"✅ Preprocessing complete. Saved to {output_path}")

if __name__ == "__main__":
    preprocess_data()
# tests/test_clean_data.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from preprocessing.clean_data import preprocess_data

def test_preprocessing_creates_output():
    preprocess_data()
    df = pd.read_csv('preprocessing/processed_data.csv')
    assert 'value_scaled' in df.columns
    assert not df.isnull().values.any()
    print("✅ Test passed!")

if __name__ == "__main__":
    test_preprocessing_creates_output()
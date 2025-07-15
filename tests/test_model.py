# tests/test_model.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.train_model import train_model
from model.predict import run_inference

def test_model_pipeline():
    train_model()
    run_inference()
    print("✅ ML pipeline test passed.")

if __name__ == "__main__":
    test_model_pipeline()
"""
Script to retrain and save the XGBoost model without gpu_id attribute
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# This script assumes you have the training data available
# For now, we'll create a workaround to fix the existing model

import joblib
import pickle
from xgboost import XGBRegressor
import numpy as np

model_path = os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'tibia_price_model.pkl')

print("Loading existing model...")
try:
    model = joblib.load(model_path)
except:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

print(f"Model type: {type(model)}")
print(f"Model attributes: {model.__dict__.keys()}")

# Remove gpu_id from all levels
def clean_model(obj, depth=0):
    """Recursively remove gpu_id from model object"""
    if depth > 10:  # Prevent infinite recursion
        return
    
    if hasattr(obj, '__dict__'):
        if 'gpu_id' in obj.__dict__:
            print(f"Removing gpu_id from {type(obj).__name__}")
            del obj.__dict__['gpu_id']
    
    # Check nested objects
    for attr_name in dir(obj):
        if not attr_name.startswith('_'):
            try:
                attr = getattr(obj, attr_name)
                if hasattr(attr, '__dict__') and not isinstance(attr, type):
                    clean_model(attr, depth + 1)
            except:
                pass

print("Cleaning model...")
clean_model(model)

# Save the cleaned model
print("Saving cleaned model...")
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")

# Verify it loads without errors
print("Verifying model loads correctly...")
try:
    test_model = joblib.load(model_path)
    print("✓ Model loaded successfully!")
except Exception as e:
    print(f"✗ Error loading model: {e}")

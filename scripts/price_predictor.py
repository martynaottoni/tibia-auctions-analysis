import joblib
import pandas as pd
import numpy as np


# Load model
model = joblib.load('notebooks/tibia_price_model.pkl')
print("Model loaded!")
print(f"Model type: {type(model)}")

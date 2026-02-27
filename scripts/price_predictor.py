import joblib
import pandas as pd
import numpy as np
import os
import sys
import xgboost as xgb

# Load model from JSON format
model_path = os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'tibia_price_model.json')
booster = xgb.Booster()
booster.load_model(model_path)
model = xgb.XGBRegressor()
model._Booster = booster

try:
    model = joblib.load(model_path)
    print(f"Model loaded successfully from {model_path}", file=sys.stderr)
except Exception as e:
    print(f"ERROR loading model from {model_path}: {e}", file=sys.stderr)
    raise

def predict_character_price(character_data):
    df = pd.DataFrame([character_data.dict()])
    
    # Calculate main_skill
    vocation_id = df['vocation_id'].values[0]
    if vocation_id == 1:
        df['main_skill'] = df[['sword', 'axe', 'club']].max(axis=1)
    elif vocation_id == 2:
        df['main_skill'] = df['distance']
    elif vocation_id in [3, 4]:
        df['main_skill'] = df['magic']
    elif vocation_id == 5:
        df['main_skill'] = df['fist']
    else:
        df['main_skill'] = df['level'] / 10
    
    df['main_skill_percentile'] = 0.5
    df['secondary_skill'] = df['shielding'] if vocation_id in [1, 2] else 0
    
    # One-hot encode weapon_type
    df['weapon_type_axe'] = (df['weapon_type'].str.lower() == 'axe').astype(int)
    df['weapon_type_club'] = (df['weapon_type'].str.lower() == 'club').astype(int)
    df['weapon_type_sword'] = (df['weapon_type'].str.lower() == 'sword').astype(int)
    
    # One-hot encode pvp_type
    df['pvp_type_Hardcore'] = (df['pvp_type'] == 'Hardcore').astype(int)
    df['pvp_type_Open'] = (df['pvp_type'] == 'Open').astype(int)
    df['pvp_type_Optional'] = (df['pvp_type'] == 'Optional').astype(int)
    df['pvp_type_Retro Hardcore'] = (df['pvp_type'] == 'Retro Hardcore').astype(int)
    df['pvp_type_Retro Open'] = (df['pvp_type'] == 'Retro Open').astype(int)
    
    # One-hot encode location
    df['location_BR'] = (df['location'] == 'BR').astype(int)
    df['location_EU'] = (df['location'] == 'EU').astype(int)
    df['location_NA'] = (df['location'] == 'NA').astype(int)
    df['location_OCE'] = (df['location'] == 'OCE').astype(int)
    
    # Select required columns in correct order
    required_cols = ['level', 'main_skill', 'main_skill_percentile', 'secondary_skill', 
                     'achievement_points', 'boss_points', 'charm_total', 'outfits_count', 
                     'mounts_count', 'store_outfits_count', 'store_mounts_count', 'vocation_id', 
                     'prey_slot', 'hunting_slot', 'charm_expansion', 'transfer', 'battleye', 
                     'weapon_type_axe', 'weapon_type_club', 'weapon_type_sword',
                     'pvp_type_Hardcore', 'pvp_type_Open', 'pvp_type_Optional', 
                     'pvp_type_Retro Hardcore', 'pvp_type_Retro Open',
                     'location_BR', 'location_EU', 'location_NA', 'location_OCE']
    
    df = df[required_cols]
    
    prediction = model.predict(df)[0]
    return float(np.expm1(prediction))


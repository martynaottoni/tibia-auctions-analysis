from fastapi import FastAPI
from pydantic import BaseModel
from scripts.price_predictor import predict_character_price

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Tibia Price Predictor API is running", "docs": "/docs"}

class CharacterInput(BaseModel):
    level: int
    vocation_id: int
    charm_total: int
    achievement_points: int
    boss_points: int
    outfits_count: int
    mounts_count: int
    store_outfits_count: int
    store_mounts_count: int
    prey_slot: bool
    hunting_slot: bool
    charm_expansion: bool
    transfer: bool
    battleye: bool
    magic: float
    axe: float
    sword: float
    club: float
    distance: float
    shielding: float
    fist: float
    weapon_type: str
    pvp_type: str
    location: str

@app.post("/predict")
def predict_price(character: CharacterInput):
    price = predict_character_price(character)
    return {"predicted_price": price}

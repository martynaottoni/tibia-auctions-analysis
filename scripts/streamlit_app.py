import streamlit as st
import requests

st.title("Tibia Character Price Predictor")
st.write("Predict the price of your character based on stats")

# Basic stats
col1, col2 = st.columns(2)
with col1:
    level = st.number_input("Level", min_value=1, max_value=500, value=100)
    vocation_id = st.selectbox("Vocation", [1, 2, 3, 4, 5], format_func=lambda x: {1: "Knight", 2: "Paladin", 3: "Druid", 4: "Sorcerer", 5: "Monk"}[x])
    charm_total = st.number_input("Charm Total", min_value=0, value=0)
    achievement_points = st.number_input("Achievement Points", min_value=0, value=0)
    boss_points = st.number_input("Boss Points", min_value=0, value=0)

with col2:
    outfits_count = st.number_input("Outfits Count", min_value=0, value=0)
    mounts_count = st.number_input("Mounts Count", min_value=0, value=0)
    store_outfits_count = st.number_input("Store Outfits Count", min_value=0, value=0)
    store_mounts_count = st.number_input("Store Mounts Count", min_value=0, value=0)

# Skills
st.subheader("Skills")

# Initialize all skills with 0
magic = 0.0
axe = 0.0
sword = 0.0
club = 0.0
distance = 0.0
shielding = 0.0
fist = 0.0
weapon_type = "sword"  # default

if vocation_id == 1:  # Knight
    st.write("**Knight - Melee Combat**")
    col3, col4 = st.columns(2)
    with col3:
        axe = st.number_input("Axe", min_value=0.0, value=0.0)
        sword = st.number_input("Sword", min_value=0.0, value=0.0)
    with col4:
        club = st.number_input("Club", min_value=0.0, value=0.0)
        shielding = st.number_input("Shielding", min_value=0.0, value=0.0)
    weapon_type = st.selectbox("Weapon Type", ["axe", "club", "sword"])
    
elif vocation_id == 2:  # Paladin
    st.write("**Paladin - Distance & Shield**")
    col3, col4 = st.columns(2)
    with col3:
        distance = st.number_input("Distance", min_value=0.0, value=0.0)
    with col4:
        shielding = st.number_input("Shielding", min_value=0.0, value=0.0)
    with col5:
        magic = st.number_input("Magic", min_value=0.0, value=0.0)
    
elif vocation_id in [3, 4]:  # Druid or Sorcerer
    st.write("**Mage - Magic**")
    magic = st.number_input("Magic", min_value=0.0, value=0.0)
    
elif vocation_id == 5:  # Monk
    st.write("**Monk - Fist Fighting**")
    col3, col4 = st.columns(2)
    with col3:
        fist = st.number_input("Fist", min_value=0.0, value=0.0)
    with col4:
        magic = st.number_input("Magic", min_value=0.0, value=0.0)


# Booleans
st.subheader("Features")
col5, col6 = st.columns(2)
with col5:
    prey_slot = st.checkbox("Prey Slot", value=False)
    hunting_slot = st.checkbox("Hunting Slot", value=False)
    charm_expansion = st.checkbox("Charm Expansion", value=False)

with col6:
    transfer = st.checkbox("Transfer", value=False)
    battleye = st.checkbox("BattlEye", value=False)

# Categorical
st.subheader("Server Info")
col7, col8 = st.columns(2)
with col7:
    pvp_type = st.selectbox("PvP Type", ["Open", "Optional", "Hardcore", "Retro Open", "Retro Hardcore"])
with col8:
    location = st.selectbox("Location", ["EU", "NA", "BR", "OCE"])

if st.button("Predict Price"):
    # Prepare data
    character_data = {
        "level": level,
        "vocation_id": vocation_id,
        "charm_total": charm_total,
        "achievement_points": achievement_points,
        "boss_points": boss_points,
        "outfits_count": outfits_count,
        "mounts_count": mounts_count,
        "store_outfits_count": store_outfits_count,
        "store_mounts_count": store_mounts_count,
        "prey_slot": prey_slot,
        "hunting_slot": hunting_slot,
        "charm_expansion": charm_expansion,
        "transfer": transfer,
        "battleye": battleye,
        "magic": magic,
        "axe": axe,
        "sword": sword,
        "club": club,
        "distance": distance,
        "shielding": shielding,
        "fist": fist,
        "weapon_type": weapon_type,
        "pvp_type": pvp_type,
        "location": location
    }
    
    # Send to API
    response = requests.post("http://127.0.0.1:8000/predict", json=character_data)
    price = response.json()["predicted_price"]
    
    st.success(f"Predicted Price: {price:.2f} TC")

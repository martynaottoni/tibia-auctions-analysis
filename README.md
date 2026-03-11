# Data-Driven Insights into MMORPG Economies: Market Analysis & Price Prediction for Tibia Auctions

**Advanced ML-powered price prediction for Tibia character auctions**  
Analyzing 1.1M+ historical records to understand character pricing dynamics

[![Live Demo](https://img.shields.io/badge/Live_Demo-Streamlit-red?style=for-the-badge)](https://tibia-auctions-analysis.streamlit.app/)
[![API Docs](https://img.shields.io/badge/API_Docs-FastAPI-green?style=for-the-badge)](https://tibia-auctions-analysis.onrender.com/docs)
[![Portfolio](https://img.shields.io/badge/Portfolio-View_Project-blue?style=for-the-badge)](https://martyna-ottoni.vercel.app/projects/analysis-of-the-tibia-auction-market-2021-2025)

## Project Highlights

- **85.8% Accuracy** - R² score on test set
- **1.1M+ Records** - Comprehensive dataset analysis
- **Production ML API** - FastAPI + XGBoost deployment
- **Interactive UI** - Streamlit web application
- **Real-time Predictions** - Character price estimation

## Tech Stack

**Data & ML:**
- Python (pandas, numpy, scikit-learn)
- XGBoost for regression modeling
- PostgreSQL for data storage
- Jupyter Notebooks for analysis

**Production:**
- FastAPI for REST API
- Streamlit for web interface
- Render for backend deployment
- Streamlit Cloud for frontend

**Visualization:**
- Plotly for interactive charts
- Seaborn for statistical plots
- Matplotlib for custom visualizations

## Key Results

| Metric | Value |
|--------|-------|
| **R² Score** | 0.8582 |
| **MAE** | 809 TC |
| **RMSE** | 1,801 TC |
| **Dataset Size** | 1.1M+ auctions |
| **Features** | 30+ engineered |

## Analysis Insights

### Key Findings
- **Level is King**: Strongest price predictor (0.66 correlation)
- **Charm Power**: Charm total is second most important (0.63 correlation)
- **Skill Matters**: Vocation-specific main skills drive pricing
- **Market Segmentation**: PvP vs PvE worlds show different patterns

### Feature Engineering
- Vocation-specific main skill calculation
- Percentile ranking within character class
- Server type and location encoding
- Achievement and cosmetic item scoring

## Live Demo

### Web Application
Try the live price predictor: [Tibia Price Predictor](https://tibia-auctions-analysis.streamlit.app/)

### API Usage
```python
import requests

# Example prediction
character = {
    "level": 500,
    "vocation_id": 1,  # Knight
    "charm_total": 4500,
    "achievement_points": 600,
    "boss_points": 1500,
    "outfits_count": 15,
    "mounts_count": 10,
    "store_outfits_count": 2,
    "store_mounts_count": 1,
    "prey_slot": True,
    "hunting_slot": True,
    "charm_expansion": True,
    "transfer": True,
    "battleye": True,
    "magic": 0.0,
    "axe": 115.0,
    "sword": 20.0,
    "club": 20.0,
    "distance": 0.0,
    "shielding": 108.0,
    "fist": 0.0,
    "weapon_type": "axe",
    "pvp_type": "Open",
    "location": "EU"
}

response = requests.post(
    "https://tibia-auctions-analysis.onrender.com/predict", 
    json=character
)
price = response.json()["predicted_price"]
print(f"Predicted price: {price:.2f} TC")
```

## Project Structure

```
tibia-auctions-analysis/
├── notebooks/
│   ├── data_exploration.ipynb          # EDA & insights
│   ├── price_analysis_modeling.ipynb   # ML model training
│   └── tibia_price_model.json          # Trained model
├── scripts/
│   ├── api.py                          # FastAPI backend
│   ├── streamlit_app.py                # Web interface
│   └── price_predictor.py              # ML inference
├── outputs/                            # Generated visualizations
└── requirements.txt                    # Dependencies
```

## Quick Start

### Local Development
```bash
# Clone repository
git clone https://github.com/martynaottoni/tibia-auctions-analysis
cd tibia-auctions-analysis

# Install dependencies
pip install -r requirements.txt

# Start API server
uvicorn scripts.api:app --reload

# Start Streamlit app (new terminal)
streamlit run scripts/streamlit_app.py
```

### API Endpoints
- `GET /` - Health check
- `POST /predict` - Character price prediction
- `GET /docs` - Interactive API documentation

## Model Performance

### Training Results
- **Algorithm**: XGBoost Regressor with log transformation
- **Training Data**: 815K+ characters
- **Validation**: 80/20 train-test split
- **Cross-validation**: 5-fold CV for hyperparameter tuning

### Feature Importance
1. **Level** (0.66) - Character level
2. **Charm Total** (0.63) - Accumulated charm points
3. **Main Skill Percentile** (0.40) - Vocation-specific skill ranking
4. **Achievement Points** (0.51) - Game achievements
5. **Cosmetic Items** (0.50) - Outfits and mounts

## Business Impact

### Problem Solved
- **Market Transparency**: Players can estimate fair character prices
- **Investment Decisions**: Data-driven character trading
- **Market Analysis**: Understanding pricing factors

### Use Cases
- Character sellers: Price optimization
- Buyers: Fair value assessment
- Market researchers: Trend analysis
- Game economists: Virtual economy insights

## Future Enhancements

- Real-time data pipeline integration
- Advanced time series forecasting
- Market trend predictions
- Mobile app development
- Multi-server price comparison

## Technical Details

### Data Pipeline
1. **Collection**: Web scraping from Tibia.com
2. **Storage**: PostgreSQL with optimized indexes
3. **Processing**: Feature engineering and cleaning
4. **Training**: XGBoost with hyperparameter tuning
5. **Deployment**: Containerized API on Render

### Model Architecture
- **Input**: 30+ engineered features
- **Algorithm**: XGBoost with log transformation
- **Output**: Character price in Tibia Coins (TC)
- **Validation**: Cross-validation and holdout testing

## Author

**Martyna Ottoni**
- Portfolio: [martyna-ottoni.vercel.app](https://martyna-ottoni.vercel.app)
- LinkedIn: [linkedin.com/in/martyna-ottoni](https://www.linkedin.com/in/martyna-ottoni-9b5723296/)
- GitHub: [@martynaottoni](https://github.com/martynaottoni)

---

**Star this repo if you found it helpful!**

*Built with care for the Tibia community*
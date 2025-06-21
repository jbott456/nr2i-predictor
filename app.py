# app.py

import streamlit as st
from model import calculate_nr2i_score
from utils.mlb_data import fetch_today_games
import pandas as pd

st.set_page_config(page_title="NR2I Predictor", layout="wide")
st.title("⚾ NR2I Predictor")
st.write("This app predicts MLB games where no runs will be scored in the **2nd inning**.")

st.subheader("📅 Today's Top Games")

# Fetch today's games
try:
    games_data = fetch_today_games()

    # Convert to DataFrame
    df = pd.DataFrame(games_data)

    # Calculate scores
    df["NR2I Score"] = df.apply(
        lambda row: calculate_nr2i_score(
            pitcher_era=row["Pitcher ERA"],
            pitcher_whip=row["Pitcher WHIP"],
            team_2nd_inning_rate=row["Team 2nd-Inning Run Rate"],
            opponent_2nd_inning_rate=row["Opponent 2nd-Inning Allowed Rate"]
        ),
        axis=1
    )

    # Add confidence and probability
    df["Model Confidence"] = df["NR2I Score"].apply(
        lambda score: "High" if score >= 0.80 else "Medium" if score >= 0.72 else "Low"
    )
    df["NR2I Probability"] = df["NR2I Score"].apply(lambda x: f"{round(x * 100)}%")

    # Show results
    st.dataframe(df[["Game", "NR2I Probability", "Model Confidence"]])

except Exception as e:
    st.error(f"⚠️ Failed to load today's MLB games: {e}")

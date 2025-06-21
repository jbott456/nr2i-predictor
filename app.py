# app.py

import streamlit as st
import pandas as pd
from model import calculate_nr2i_score
from utils.mlb_data import fetch_today_games

st.set_page_config(page_title="NR2I Predictor", layout="wide")
st.title("⚾ NR2I Predictor")
st.write("This app predicts MLB games where no runs will be scored in the **2nd inning** based on pitching and scoring data.")

st.subheader("📅 Today's Top NR2I Picks")

try:
    games_data = fetch_today_games()

    if not games_data:
        st.warning("No MLB games found for today.")
    else:
        df = pd.DataFrame(games_data)

        df["NR2I Score"] = df.apply(
            lambda row: calculate_nr2i_score(
                pitcher_era=row.get("Pitcher ERA", 4.00),
                pitcher_whip=row.get("Pitcher WHIP", 1.30),
                team_2nd_inning_rate=row.get("Team 2nd-Inning Run Rate", 0.35),
                opponent_2nd_inning_rate=row.get("Opponent 2nd-Inning Allowed Rate", 0.35),
            ),
            axis=1
        )

        df["Model Confidence"] = df["NR2I Score"].apply(
            lambda score: "High" if score >= 0.80 else "Medium" if score >= 0.72 else "Low"
        )
        df["NR2I Probability"] = df["NR2I Score"].apply(lambda x: f"{round(x * 100)}%")

        # Sort by best score
        df = df.sort_values(by="NR2I Score", ascending=False)

        # Prepare display DataFrame
        display_df = df[[
            "Game", "Pitcher", "Pitcher ERA", "Pitcher WHIP",
            "Team 2nd-Inning Run Rate", "Opponent 2nd-Inning Allowed Rate",
            "NR2I Probability", "Model Confidence"
        ]]

        # Apply highlight styling
        def highlight_row(row):
            color = "#c6f6d5" if row["Model Confidence"] == "High" else \
                    "#fefcbf" if row["Model Confidence"] == "Medium" else \
                    "#bee3f8"
            return [f"background-color: {color}"] * len(row)

        st.dataframe(display_df.style.apply(highlight_row, axis=1))

except Exception as e:
    st.error(f"⚠️ Failed to load today's MLB games: {e}")

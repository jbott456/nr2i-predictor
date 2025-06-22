import streamlit as st
import pandas as pd
from model import calculate_nr2i_score
from utils.mlb_data import fetch_today_games

# Page setup
st.set_page_config(page_title="NR2I Predictor", layout="wide")
st.title("⚾ NR2I Predictor")
st.write("This app predicts MLB games where no runs will be scored in the **2nd inning** based on pitching and scoring data.")

st.subheader("📅 Today's Top NR2I Picks")

try:
    # Pull today's matchups and data
    games_data = fetch_today_games()

    if not games_data:
        st.warning("No MLB games found for today.")
    else:
        # Convert games_data into DataFrame
        df = pd.DataFrame(games_data)

        # Debugging: Check the DataFrame structure
        st.write("DataFrame Columns:", df.columns)
        st.write("First few rows of the DataFrame:", df.head())

        # Compute NR2I Score
        df["NR2I Score"] = df.apply(
            lambda row: calculate_nr2i_score(
                pitcher_era=row.get("Pitcher ERA", 4.00),
                pitcher_whip=row.get("Pitcher WHIP", 1.30),
                team_2nd_inning_rate=row.get("Team 2nd-Inning Run Rate", 0.35),
                opponent_2nd_inning_rate=row.get("Opponent 2nd-Inning Allowed Rate", 0.35),
            ),
            axis=1
        )

        # Add model outputs
        df["Model Confidence"] = df["NR2I Score"].apply(
            lambda score: "High" if score >= 0.80 else "Medium" if score >= 0.72 else "Low"
        )
        df["NR2I Probability"] = df["NR2I Score"].apply(lambda x: f"{round(x * 100)}%")

        # Reorder columns for display (modify based on actual DataFrame structure)
        display_df = df[[
            "Game", "Away Pitcher", "Home Pitcher", "Away Recent 2nd Inning Rate", 
            "Home Recent 2nd Inning Rate", "Pitcher ERA", "Pitcher WHIP",
            "Team 2nd-Inning Run Rate", "Opponent 2nd-Inning Allowed Rate",
            "NR2I Probability", "Model Confidence"
        ]] 

        # Sort by NR2I Probability and display
        display_df = display_df.sort_values(by="NR2I Probability", ascending=False)
        
        # Highlight rows based on NR2I probability
        def highlight_rows(row):
            if row["NR2I Probability"] > 80:
                return ['background-color: green'] * len(row)
            elif row["NR2I Probability"] > 70:
                return ['background-color: yellow'] * len(row)
            else:
                return ['background-color: lightblue'] * len(row)

        # Display dataframe with styles
        st.dataframe(display_df.style.apply(highlight_rows, axis=1))

except Exception as e:
    st.error(f"⚠️ Failed to load today's MLB games: {e}")

import streamlit as st

st.set_page_config(page_title="NR2I Predictor", layout="wide")

st.title("⚾ NR2I Predictor")
st.write("This app predicts MLB games where no runs will be scored in the **2nd inning**.")

st.subheader("📅 Today's Top Games")

games = {
    "Game": ["Royals @ Padres", "Astros @ Angels", "Mets @ Phillies"],
    "NR2I Probability": ["85%", "85%", "80%"],
    "Model Confidence": ["High", "High", "Medium"]
}

st.dataframe(games)

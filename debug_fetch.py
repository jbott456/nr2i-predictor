# debug_fetch.py

import streamlit as st
from utils.mlb_data import fetch_today_games

st.set_page_config(page_title="Debug Fetch", layout="wide")
st.title("🔍 Debug: ESPN JSON Data Fetch")

try:
    games = fetch_today_games()
    st.success(f"✅ Returned {len(games)} games")
    st.subheader("Sample Fetched Data:")
    st.json(games[:5])  # Show top 5
except Exception as e:
    st.error(f"❌ Fetch failed: {e}")


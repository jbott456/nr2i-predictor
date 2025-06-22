import streamlit as st
from utils.mlb_data import fetch_today_games

st.title("🔍 Debug: ESPN MLB Fetch")

try:
    games = fetch_today_games()

    if not games:
        st.error("❌ No games returned from ESPN API")
    else:
        st.success(f"✅ {len(games)} games found")
        for game in games:
            st.write(game)
except Exception as e:
    st.error(f"⚠️ Error fetching games: {e}")



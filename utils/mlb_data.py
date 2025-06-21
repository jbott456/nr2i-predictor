# utils/mlb_data.py

import requests
from bs4 import BeautifulSoup

def fetch_today_games():
    url = "https://www.espn.com/mlb/schedule"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    games = []
    for row in soup.select("table tbody tr"):
        cols = row.find_all("td")
        if len(cols) < 2:
            continue

        away_team = cols[0].text.strip()
        home_team = cols[1].text.strip()
        matchup = f"{away_team} @ {home_team}"

        games.append({
            "Game": matchup,
            # Placeholder values below — we’ll replace next
            "Pitcher ERA": 3.50,
            "Pitcher WHIP": 1.20,
            "Team 2nd-Inning Run Rate": 0.40,
            "Opponent 2nd-Inning Allowed Rate": 0.40
        })

    return games

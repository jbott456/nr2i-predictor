# utils/mlb_data.py

import requests
from bs4 import BeautifulSoup
import re

def fetch_today_games():
    url = "https://www.espn.com/mlb/schedule"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    games = []

    for section in soup.find_all("section", class_="Card"):
        table = section.find("table")
        if not table:
            continue

        for row in table.select("tbody tr"):
            cols = row.find_all("td")
            if len(cols) < 2:
                continue

            teams_text = cols[0].get_text(separator="|").split("|")
            if len(teams_text) != 2:
                continue

            away_team = teams_text[0].strip()
            home_team = teams_text[1].strip()
            matchup = f"{away_team} @ {home_team}"

            # Try to get starting pitchers and ERA from col[1]
            pitcher_info = cols[1].get_text().strip()
            era_match = re.findall(r'\d+\.\d+', pitcher_info)
            pitcher_era = float(era_match[0]) if era_match else 4.00  # fallback

            games.append({
                "Game": matchup,
                "Pitcher ERA": pitcher_era,
                "Pitcher WHIP": 1.30,  # Placeholder WHIP
                "Team 2nd-Inning Run Rate": 0.35,  # Placeholder
                "Opponent 2nd-Inning Allowed Rate": 0.35  # Placeholder
            })

    return games

# utils/mlb_data.py

import requests
from bs4 import BeautifulSoup
import re

def fetch_today_games():
    schedule_url = "https://www.espn.com/mlb/schedule"
    resp = requests.get(schedule_url)
    soup = BeautifulSoup(resp.text, "html.parser")

    games = []
    # New layout: every <article> represents a game
    for game_card in soup.select("article"):
        teams = game_card.select_one("span.logo-nw") and game_card.find_all("span", class_="sb-team-short")
        pitcher_info = game_card.select_one("div:has(strong)")

        if not teams or len(teams) != 2:
            continue

        away_team = teams[0].text.strip()
        home_team = teams[1].text.strip()
        matchup = f"{away_team} @ {home_team}"

        era, whip = 4.00, 1.30
        if pitcher_info:
            text = pitcher_info.get_text()
            era_match = re.search(r"ERA\s?(\d+\.\d+)", text)
            whip_match = re.search(r"WHIP\s?(\d+\.\d+)", text)
            if era_match: era = float(era_match.group(1))
            if whip_match: whip = float(whip_match.group(1))

        games.append({
            "Game": matchup,
            "Pitcher ERA": era,
            "Pitcher WHIP": whip,
            "Team 2nd-Inning Run Rate": 0.38,
            "Opponent 2nd-Inning Allowed Rate": 0.39
        })

    return games

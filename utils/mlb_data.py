# utils/mlb_data.py

import requests
from datetime import date

def fetch_today_games():
    today = date.today().strftime("%Y%m%d")
    url = f"https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates={today}"
    resp = requests.get(url)
    
    if resp.status_code != 200:
        return []

    data = resp.json()
    events = data.get("events", [])
    
    games = []
    for event in events:
        try:
            home = event["competitions"][0]["competitors"][0]
            away = event["competitions"][0]["competitors"][1]
            
            home_team = home["team"]["shortDisplayName"]
            away_team = away["team"]["shortDisplayName"]
            
            matchup = f"{away_team} @ {home_team}"
            
            games.append({
                "Game": matchup,
                # Placeholder pitching/stats values (until we fetch actual starters)
                "Pitcher ERA": 3.50,
                "Pitcher WHIP": 1.20,
                "Team 2nd-Inning Run Rate": 0.40,
                "Opponent 2nd-Inning Allowed Rate": 0.40
            })
        except Exception as e:
            continue

    return games

import requests
from datetime import date

def fetch_today_games():
    today = date.today().strftime("%Y%m%d")
    url = f"https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates={today}"
    resp = requests.get(url)
    data = resp.json()

    games = []
    for evt in data.get("events", []):
        comp = evt["competitions"][0]
        teams = comp["competitors"]

        away = next(t for t in teams if t["homeAway"] == "away")
        home = next(t for t in teams if t["homeAway"] == "home")

        matchup = f"{away['team']['displayName']} @ {home['team']['displayName']}"

        # Probable pitchers
        away_pitcher = away.get("probablePitcher", {}).get("fullName")
        home_pitcher = home.get("probablePitcher", {}).get("fullName")

        # Stats from JSON if available (some levels include average ERA/WHIP), otherwise placeholders
        era = away.get("probablePitcherStats", {}).get("era", 4.00)
        whip = away.get("probablePitcherStats", {}).get("whip", 1.30)

        games.append({
            "Game": matchup,
            "Pitcher ERA": float(era),
            "Pitcher WHIP": float(whip),
            "Team 2nd-Inning Run Rate": 0.38,
            "Opponent 2nd-Inning Allowed Rate": 0.39
        })

    return games


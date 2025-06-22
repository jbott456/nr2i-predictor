import requests
from datetime import datetime

# Define mock second-inning run rates (you can adjust this based on available data)
TEAM_2ND_INNING_RUN_RATE = {
    "NYY": 0.34, "BOS": 0.37, "LAD": 0.36, "ATL": 0.38,
    "HOU": 0.33, "CHC": 0.32, "SF": 0.31, "PHI": 0.39,
    "NYM": 0.35, "SD": 0.30, "OAK": 0.29, "PIT": 0.27,
    "CIN": 0.34, "CLE": 0.33, "KC": 0.28, "TB": 0.36
    # Add more teams as needed
}

MLB_API_URL = "https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={date}&hydrate=team,linescore,probablePitcher(stats(type=season,season=2024))"

def fetch_today_games():
    today = datetime.today().strftime('%Y-%m-%d')
    url = MLB_API_URL.format(date=today)
    resp = requests.get(url)
    data = resp.json()

    games = []
    for date in data.get("dates", []):
        for game in date.get("games", []):
            teams = game.get("teams", {})
            away_team = teams.get("away", {}).get("team", {}).get("name", "")
            home_team = teams.get("home", {}).get("team", {}).get("name", "")
            game_matchup = f"{away_team} @ {home_team}"

            away_pitcher_data = teams.get("away", {}).get("probablePitcher", {})
            pitcher_name = away_pitcher_data.get("fullName", "N/A")
            stats = away_pitcher_data.get("stats", [{}])[0].get("splits", [{}])[0].get("stat", {})
            era = float(stats.get("era", 4.00))
            whip = float(stats.get("whip", 1.30))

            away_abbr = teams.get("away", {}).get("team", {}).get("abbreviation", "")
            home_abbr = teams.get("home", {}).get("team", {}).get("abbreviation", "")

            team_rate = TEAM_2ND_INNING_RUN_RATE.get(away_abbr, 0.35)
            opp_rate = TEAM_2ND_INNING_RUN_RATE.get(home_abbr, 0.35)

            games.append({
                "Game": game_matchup,
                "Away Pitcher": pitcher_name,
                "Home Pitcher": "",  # Placeholder, update if you fetch Home Pitcher data
                "Pitcher ERA": era,
                "Pitcher WHIP": whip,
                "Team 2nd-Inning Run Rate": team_rate,
                "Opponent 2nd-Inning Allowed Rate": opp_rate
            })

    return games

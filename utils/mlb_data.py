# utils/mlb_data.py

import requests
from datetime import datetime

# Map team abbreviations or names to 2nd-inning run rates (mock values for now)
TEAM_2ND_INNING_RUN_RATE = {
    "NYY": 0.34, "BOS": 0.37, "LAD": 0.36, "ATL": 0.38,
    "HOU": 0.33, "CHC": 0.32, "SF": 0.31, "PHI": 0.39,
    "NYM": 0.35, "SD": 0.30, "OAK": 0.29, "PIT": 0.27,
    "CIN": 0.34, "CLE": 0.33, "KC": 0.28, "TB": 0.36
}

MLB_API_URL = "https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={date}&hydrate=team,linescore,probablePitcher(stats(type=season,season=2024))"

# Fetch last 8 games data of a pitcher
def get_pitcher_history(pitcher_id):
    url = f"https://statsapi.mlb.com/api/v1/people/{pitcher_id}/stats?stats=gameLog&gameType=R&season=2024"
    response = requests.get(url)
    data = response.json()

    games_analyzed = 0
    second_inning_runs = 0

    for game in data.get("stats", []):
        game_stats = game.get("splits", [])
        if game_stats:
            game = game_stats[0]
            innings = game.get("stat", {}).get("inningsPitched", 0)
            earned_runs = game.get("stat", {}).get("earnedRuns", 0)

            # If the second inning had a run (mock logic - you can adjust)
            if "2nd" in game.get("inningSummary", []):
                second_inning_runs += 1

            games_analyzed += 1

        if games_analyzed == 8:
            break

    recent_2nd_inning_run_rate = second_inning_runs / games_analyzed if games_analyzed else 0
    return {"recent_2nd_inning_run_rate": recent_2nd_inning_run_rate}

# Fetch today’s games and add pitcher history
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
            away_pitcher_id = away_pitcher_data.get("id", None)
            away_pitcher_name = away_pitcher_data.get("fullName", "N/A")

            home_pitcher_data = teams.get("home", {}).get("probablePitcher", {})
            home_pitcher_id = home_pitcher_data.get("id", None)
            home_pitcher_name = home_pitcher_data.get("fullName", "N/A")

            # Fetch recent 2nd inning run rate for each pitcher
            away_pitcher_history = get_pitcher_history(away_pitcher_id) if away_pitcher_id else {}
            home_pitcher_history = get_pitcher_history(home_pitcher_id) if home_pitcher_id else {}

            games.append({
                "Game": game_matchup,
                "Away Pitcher": away_pitcher_name,
                "Home Pitcher": home_pitcher_name,
                "Away Recent 2nd Inning Rate": away_pitcher_history.get("recent_2nd_inning_run_rate", 0),
                "Home Recent 2nd Inning Rate": home_pitcher_history.get("recent_2nd_inning_run_rate", 0)
            })

    return games

# utils/mlb_data.py

import requests
from datetime import datetime

# Map team abbreviations or names to 2nd-inning run rates (mock values for now)
TEAM_2ND_INNING_RUN_RATE = {
    "NYY": 0.34, "BOS": 0.37, "LAD": 0.36, "ATL": 0.38,
    "HOU": 0.33, "CHC": 0.32, "SF": 0.31, "PHI": 0.39,
    "NYM": 0.35, "SD": 0.30, "OAK": 0.29, "PIT": 0.27,
    "CIN": 0.34, "CLE": 0.33, "KC": 0.28, "TB": 0.36
    # Add more teams as needed
}

MLB_API_URL = "https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={date}&hydrate=team,linescore,probablePitcher(stats(t
            opp_rate = TEAM_2ND_INNING_RUN_RATE.get(home_abbr, 0.35)

            games.append({
                "Game": game_matchup,
                "Pitcher": pitcher_name,
                "Pitcher ERA": era,
                "Pitcher WHIP": whip,
                "Team 2nd-Inning Run Rate": team_rate,
                "Opponent 2nd-Inning Allowed Rate": opp_rate
            })

    return games

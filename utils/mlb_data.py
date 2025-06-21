import requests
import re

def fetch_today_games():
    url = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"
    resp = requests.get(url)
    games_json = resp.json()

    matchups = []

    for event in games_json.get("events", []):
        try:
            competition = event["competitions"][0]
            teams = competition["competitors"]

            home = next(t for t in teams if t["homeAway"] == "home")["team"]["displayName"]
            away = next(t for t in teams if t["homeAway"] == "away")["team"]["displayName"]
            game_title = f"{away} @ {home}"

            # Default values in case no pitcher data found
            era, whip = 4.00, 1.30

            # Extract probable pitchers
            for team in teams:
                athlete = team.get("probablePitcher", {}).get("athlete")
                stats = team.get("probablePitcher", {}).get("stats", [])
                if athlete and stats:
                    stat_line = stats[0]
                    era_match = re.search(r"ERA:\s*([\d.]+)", stat_line)
                    whip_match = re.search(r"WHIP:\s*([\d.]+)", stat_line)
                    if era_match:
                        era = float(era_match.group(1))
                    if whip_match:
                        whip = float(whip_match.group(1))
                    break  # Use the first valid pitcher

            matchups.append({
                "Game": game_title,
                "Pitcher ERA": era,
                "Pitcher WHIP": whip,
                "Team 2nd-Inning Run Rate": 0.35,
                "Opponent 2nd-Inning Allowed Rate": 0.35
            })
        except Exception:
            continue

    return matchups

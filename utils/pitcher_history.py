import requests

# Fetch Pitcher History: Last 8 games
def get_pitcher_history(pitcher_id):
    # MLB Stats API URL for pitcher data
    url = f"https://statsapi.mlb.com/api/v1/people/{pitcher_id}/stats?stats=gameLog&gameType=R&season=2024"
    
    # Fetch data
    response = requests.get(url)
    data = response.json()

    # Initialize variables
    games_analyzed = 0
    second_inning_runs = 0

    # Loop through the games data
    for game in data.get("stats", []):
        game_stats = game.get("splits", [])
        
        if game_stats:
            game = game_stats[0]  # We are just interested in the first split
            innings = game.get("stat", {}).get("inningsPitched", 0)
            earned_runs = game.get("stat", {}).get("earnedRuns", 0)
            hits = game.get("stat", {}).get("hits", 0)

            # Check if runs were scored in the second inning
            inning_summary = game.get("inningSummary", [])
            
            # Assuming inningSummary has a structure like: [ "1st", "2nd", "3rd", ...]
            if "2nd" in inning_summary and earned_runs > 0:
                second_inning_runs += 1

            games_analyzed += 1

        if games_analyzed == 8:
            break  # Stop after 8 games

    # Calculate recent 2nd inning run rate
    if games_analyzed > 0:
        recent_2nd_inning_run_rate = second_inning_runs / games_analyzed
    else:
        recent_2nd_inning_run_rate = 0  # Default to 0 if no games

    return {
        "games_analyzed": games_analyzed,
        "second_inning_runs_allowed": second_inning_runs,
        "recent_2nd_inning_run_rate": recent_2nd_inning_run_rate
    }

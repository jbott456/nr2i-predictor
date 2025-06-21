def score_game(era, team_2nd_rate):
    league_base = 0.72
    if era <= 3.00:
        factor = 0.85
    elif era <= 4.00:
        factor = 0.75
    else:
        factor = 0.65
    return round(league_base * factor * (1 - team_2nd_rate), 4)

def implied_prob(odds):
    if odds > 0:
        return round(100 / (odds + 100), 4)
    else:
        return round(-odds / (-odds + 100), 4)

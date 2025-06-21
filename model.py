# model.py

BASE_PROB = 0.72

def get_factor(value, thresholds=(3.00, 4.00)):
    if value <= thresholds[0]:
        return 0.85
    elif value <= thresholds[1]:
        return 0.75
    else:
        return 0.65

def calculate_nr2i_score(pitcher_era, pitcher_whip, team_2nd_inning_rate, opponent_2nd_inning_rate):
    era_factor = get_factor(pitcher_era)
    whip_factor = get_factor(pitcher_whip, thresholds=(1.10, 1.30))
    offense_factor = 1 - team_2nd_inning_rate
    defense_factor = 1 - opponent_2nd_inning_rate

    score = BASE_PROB * era_factor * whip_factor * offense_factor * defense_factor
    return round(score, 4)

def implied_prob(odds):
    if odds > 0:
        return round(100 / (odds + 100), 4)
    else:
        return round(-odds / (-odds + 100), 4)

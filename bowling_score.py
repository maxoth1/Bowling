def bowling_score(rolls):
    i = 0                    # Index für aktuellen Wurf 
    score = 0                # Gesamtscore des Spiels
    round_index = 1          # Rundenzähler 
    round_scores = []        # Punkte jeder Runde
    visualization = []       # Darstellung  "X" für Strike und "/" für Spare

    while round_index <= 10:
        if rolls[i] == 10:
            # Strike 
            points = 10 + rolls[i+1] + rolls[i+2]
            score += points
            round_scores.append(points)
            visualization.append(["X", ""])
            i += 1  # Nur ein Wurf bei Strike
        elif rolls[i] + rolls[i+1] == 10:
            # Spare
            points = 10 + rolls[i+2]
            score += points
            round_scores.append(points)
            visualization.append([rolls[i], "/"])
            i += 2  # Zwei Würfe bei Spare
        else:
            # Normale Runde
            points = rolls[i] + rolls[i+1]
            score += points
            round_scores.append(points)
            visualization.append([rolls[i], rolls[i+1]])
            i += 2
        round_index += 1

    return score, visualization, round_scores


def bowling_score(rolls):

    """
    Berechnet den Score eines Bowlingspiels mit 10 Runden.
    
    Strike: 10 + nächste 2 Würfe  
    Spare: 10 + nächster Wurf  
    Normal: Summe aus 2 Würfen

    Erweiterung:
    round_index zählt die Runden (1–10)
    round_scores speichert Punkte je Runde
    visualization zeigt "X" für Strike und "/" für Spare


    """


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
            i += 1  
        elif rolls[i] + rolls[i+1] == 10:
            # Spare
            points = 10 + rolls[i+2]
            score += points
            round_scores.append(points)
            visualization.append([rolls[i], "/"])
            i += 2  
        else:
            # Normale Runde
            points = rolls[i] + rolls[i+1]
            score += points
            round_scores.append(points)
            visualization.append([rolls[i], rolls[i+1]])
            i += 2
        round_index += 1

    return score, visualization, round_scores


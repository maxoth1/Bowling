def bowling_score(rolls):

    """
    Berechnet den Score eines Bowlingspiels mit 10 Runden.
    
    Strike: 10 + nächste 2 Würfe  
    Spare: 10 + nächster Wurf  
    Normal: Summe aus 2 Würfen
    """
    i = 0         # Index für aktuellen Wurf
    score = 0     # Gesamtscore des Spiels

    for _ in range(10):  
        if rolls[i] == 10:
            # Strike
            score += 10 + rolls[i+1] + rolls[i+2]
            i += 1
        elif rolls[i] + rolls[i+1] == 10:
            # Spare
            score += 10 + rolls[i+2]
            i += 2
        else:
            # Normale Runde
            score += rolls[i] + rolls[i+1]
            i += 2

    return score

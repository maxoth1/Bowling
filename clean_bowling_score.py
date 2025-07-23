def bowling_score(rolls):

    #Berechnet den Endstand eines Bowlingspiels (rolls).
    #- Strike = 10 Punkte + nächste 2 Würfe
    #- Spare  = 10 Punkte + nächster Wurf
    #- Normal = Summe 2 Würfe


    i = 0         # Index für aktuellen Wurf
    score = 0     # Gesamtscore des Spiels

    for _ in range(10):  # Ein Spiel besteht aus 10 Runden
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

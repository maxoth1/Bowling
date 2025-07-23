import random
from bowling_score import bowling_score

def generate_random_rolls():
    rolls = []
    for _ in range(10):
        first = random.randint(0, 10)
        if first == 10:
            # Strike
            rolls.append(10)
        else:
            second = random.randint(0, 10 - first)
            rolls.extend([first, second])

    # Bonuswürfe 
    if rolls[-1] == 10:
        rolls.extend([random.randint(0, 10), random.randint(0, 10)])
    elif rolls[-2] + rolls[-1] == 10:
        rolls.append(random.randint(0, 10))

    return rolls

# Haupttestlauf
if __name__ == "__main__":
    rolls = generate_random_rolls()                                 # Zufällige Würfe erzeugen
    score, visualization, round_scores = bowling_score(rolls)      # Auswertung durchführen

    print("Bowling-Game:")
    print("=" * 30)
    for i in range(10):
        throw1, throw2 = visualization[i]                          
        print(f"Round {i+1}: {throw1}\t{throw2}\t→ {round_scores[i]} Punkte")
    print("=" * 30)
    print(f"Gesamtpunktzahl: {score}")
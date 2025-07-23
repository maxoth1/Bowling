# Bowling Score – Python-Auswertung eines Bowlingspiels

## Dateien im Überblick

### `clean_bowling_score.py`
Minimalistische und funktionale Lösung zur Berechnung der Gesamtpunktzahl eines Bowlingspiels.  
Diese Version war mein Einstieg und diente zur Validierung der Grundlogik (Strike, Spare, Normalwurf).

### `bowling_score.py`
Erweiterung der Grundversion:
- Ausgabe pro Runde
- Visualisierung von Strike (`X`) und Spare (`/`)
- Punktestand für jede Runde  
Die Funktion ist besser nachvollziehbar und transparenter für Tests und spätere Erweiterungen.

### `unittest_bowling.py`
Test-Suite auf Basis des `unittest`-Moduls.  
Sie wurde **testgetrieben** entwickelt – also vor der finalen Implementierung der Funktion.  
Folgende Szenarien werden abgedeckt:
- Gutter Game (nur Fehlwürfe)
- All Ones
- Perfect Game
- 10 Spares + Bonuswurf
- Strike im letzten Frame
- Spare im letzten Frame
- Zufallsspiel
- Ungültige Eingaben (zu wenig oder zu viele Würfe)

### `bowling_game.drawio.png`
Einfache Visualisierung des Spielablaufs.  
Das Diagramm zeigt, wie ich vor dem Codieren die `if-elif-else`-Struktur entwickelt habe, basierend auf möglichen Spielsituationen.

---

## Vorgehen

Vor dem Coden habe ich die Spielmechanik grafisch modelliert, um ein sauberes Verständnis für die Entscheidungslogik (Strike, Spare, Normalwurf) zu entwickeln.  
Daraufhin habe ich mit Unittests begonnen, um typische Spielverläufe zu simulieren. Erst danach entstand die Grundfunktion (`clean_bowling_score.py`).  

Diese wurde später erweitert (`bowling_score.py`), um das Spiel auch pro Runde auszugeben und verständlich zu visualisieren.

---

## Hinweis

Alle Dateien (`clean`, `bowling_score`, `unittest`, `drawio`) gehören für mich zur Gesamtlösung.  
Sie zeigen den Lösungsweg – von der Idee über Tests bis zur funktionierenden und überprüfbaren Auswertung.

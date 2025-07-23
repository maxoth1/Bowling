# Bowling Score – Python-Auswertung eines Bowlingspiels

## Dateien im Überblick

- **clean_bowling_score.py**  
  Erste Version der Lösung. Kompakte und funktionale Implementierung zur Berechnung der Gesamtpunktzahl eines Bowlingspiels (Strike, Spare, Normalwurf).  
  Diese Version war mein Einstieg und diente zur Überprüfung der Logik.

- **bowling_score.py**  
  Erweiterung der Grundversion:  
  - Ausgabe pro Runde  
  - Visualisierung von Strike (X) und Spare (/)  
  - Punktestand für jede Runde  
  Die Funktion basiert auf derselben Logik, ist aber besser nachvollziehbar und für Tests transparenter.

- **test_bowling.py**  
  Ergänzende Datei zur Simulation eines zufälligen Spiels mit Ausgabe aller Runden.  
  Diese Datei war mein Versuch, das System auch außerhalb manueller Eingaben zu testen. Die Zufallswürfe orientieren sich an den Regeln (max. 10 Pins pro Runde, Bonuswürfe am Ende).

- **bowling_game.drawio.png**  
  Eine einfache Visualisierung der Logik, wie ich sie vor dem Codieren grob im Kopf hatte.  
  Das Diagramm zeigt, wie das Spiel funktioniert und wie ich mir die if-elif-else-Struktur hergeleitet habe.

## Vorgehen

Bevor ich mit dem Coden begonnen habe, habe ich den Bewertungsprozess des Spiels visuell modelliert.  
Das half mir, die Entscheidungslogik (Strike, Spare, Normalwurf) zu strukturieren und sauber in Code zu überführen.

Die erste Version (`clean_bowling_score.py`) habe ich genutzt, um die grundlegende Logik zu validieren.  
Auf dieser Basis habe ich die Funktionen schrittweise erweitert und eine zusätzliche Datei erstellt, um Zufallstests durchzuführen.

## Hinweis

Alle drei Dateien (`clean`, `bowling_score`, `test`) gehören für mich zur Gesamtarbeit.  
Sie zeigen den Weg von der ersten Idee bis zur ausführbaren Lösung.

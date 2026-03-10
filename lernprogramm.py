"""
================================================================================
INTERAKTIVES LERNPROGRAMM FÜR ELIAS
Themen: Punktnotation, Listen, Strings, Import & Random
================================================================================

Willkommen Elias! 
Dieses Programm ist dein interaktiver Python-Kurs.
Lies dir die Erklärungen durch und löse die Aufgaben an den markierten Stellen.
"""

# import: Hiermit laden wir externe Module. 
# random hilft uns, zufällige Dinge zu tun.
import random 

def lektion_1_strings_und_punktnotation():
    """
    LEKTION 1: Strings (Zeichenketten) und Punktnotation
    Strings sind Texte in Anführungszeichen.
    Mit der Punktnotation (z.B. text.lower()) rufen wir Funktionen auf, 
    die direkt zu diesem Datentyp gehören.
    """
    print("=== Lektion 1 ===")
    
    # print: Gibt Text in der Konsole aus
    print("Lass uns Strings untersuchen!")
    
    # input: Wartet auf eine Eingabe des Benutzers im Terminal
    wort = input("Bitte gib ein beliebiges Wort ein: ")
    
    # type: Zeigt uns den Datentyp an
    print("Der Typ deiner Eingabe ist:", type(wort))
    
    # .lower(): Macht den String zu Kleinbuchstaben
    klein_wort = wort.lower()
    print("In Kleinbuchstaben:", klein_wort)
    
    # .islower(): Prüft, ob alles kleingeschrieben ist (True/False)
    print("Ist es komplett kleingeschrieben?", klein_wort.islower())
    
    # .isalpha(): Prüft, ob der String nur aus Buchstaben besteht (keine Zahlen/Zeichen)
    print("Besteht es nur aus Buchstaben?", wort.isalpha())

    print("\n--- DEINE AUFGABE 1 ---")
    # AUFGABE 1:
    # 1. Frage den Benutzer nach seinem Namen mit 'input'.
    # 2. Speichere den Namen in einer Variablen.
    # 3. Prüfe mit '.isalpha()', ob der Name nur aus Buchstaben besteht.
    #    Tipp: nutze eine if-Abfrage -> if name.isalpha():
    # 4. Wenn ja, gib den Namen in Kleinbuchstaben (.lower()) aus.
    # 5. Wenn nein, gib aus "Das ist kein gültiger Name."
    
    # ---> SCHREIBE DEINEN CODE HIER UNTER DIESER ZEILE:
    pass


def lektion_2_listen_und_indizes():
    """
    LEKTION 2: Listen, Indizes und Methoden
    Listen können mehrere Elemente gleichzeitig speichern.
    """
    print("\n=== Lektion 2 ===")
    
    meine_liste = ["Apfel", "Banane", "Kirsche"]
    
    # len: Gibt die Länge (Anzahl der Elemente) zurück
    print("Anzahl der Elemente:", len(meine_liste))
    
    # .append: Hängt ein Element hinten an die Liste an
    meine_liste.append("Orange")
    
    # .insert: Fügt ein Element an einem bestimmten Index (Position) ein.
    # Achtung: Indizes beginnen in Python bei 0!
    meine_liste.insert(1, "Mango") 
    
    # .extend: Hängt mehrere Elemente aus einer anderen Liste an
    neue_fruechte = ["Kiwi", "Melone"]
    meine_liste.extend(neue_fruechte)
    
    print("Aktuelle Liste:", meine_liste)
    
    # Index eine andere Zuweisung geben: Wir ändern das erste Element (Index 0)
    meine_liste[0] = "Birne"
    print("Nach Zuweisung an Index 0:", meine_liste)
    
    # .remove: Entfernt ein bestimmtes Element nach Wert
    meine_liste.remove("Banane")
    
    # .pop: Entfernt ein Element an einem bestimmten Index und gibt es zurück (Standard ist das letzte)
    letztes = meine_liste.pop()
    print("Wir haben", letztes, "mit .pop() entfernt.")
    
    # .clear: Leert die gesamte Liste
    meine_liste.clear()
    print("Nach .clear() ist die Liste leer:", meine_liste)

    print("\n--- DEINE AUFGABE 2 ---")
    # AUFGABE 2:
    # 1. Erstelle eine leere Liste namens 'buchstaben'.
    # 2. Hänge (.append) die Buchstaben "a" und "c" an die Liste an (nacheinander).
    # 3. Füge (.insert) das "b" an der richtigen Stelle (Index 1) ein, damit es "a", "b", "c" ist.
    # 4. Erweitere (.extend) die Liste um ["d", "e"].
    # 5. Gib die fertige Liste mit 'print' aus.
    
    # ---> SCHREIBE DEINEN CODE HIER UNTER DIESER ZEILE:
    pass


def lektion_3_schleifen_und_random():
    """
    LEKTION 3: Schleifen (range, break, continue) und Random
    Hiermit können wir Dinge wiederholen und den Zufall nutzen.
    """
    print("\n=== Lektion 3 ===")
    
    # range: Generiert eine Zahlenfolge, hier von 0 bis 4 (insgesamt 5 Zahlen)
    print("Eine Schleife mit range(5):")
    for zahl in range(5):
        # continue: Überspringt den Rest dieses Schleifendurchlaufs und macht direkt beim Nächsten weiter
        if zahl == 2:
            print("  Überspringe die 2 mit 'continue'")
            continue
            
        # break: Bricht die gesamte Schleife sofort komplett ab
        if zahl == 4:
            print("  Breche die Schleife bei 4 ab mit 'break'")
            break
            
        print("  Zahl:", zahl)
        
    # enumerate: Gibt dir Element UND Index der Liste gleichzeitig
    tiere = ["Hund", "Katze", "Maus"]
    print("\nSchleife mit enumerate:")
    for index, tier in enumerate(tiere):
        print("Index", index, "ist das Tier", tier)
        
    # random.choice: Wählt ein zufälliges Element aus einer Liste
    zufalls_tier = random.choice(tiere)
    print("\nZufälliges Tier:", zufalls_tier)
    
    # .join: Verbindet eine Liste von Strings zu einem einzigen String.
    # Wir benutzen ein Leerzeichen " " als Klebstoff zwischen den Wörtern.
    satz_teile = ["Python", "macht", "mega", "viel", "Spaß!"]
    satz = " ".join(satz_teile)
    print("Zusammengefügt mit .join:", satz)

    print("\n--- DEINE AUFGABE 3 ---")
    # AUFGABE 3:
    # 1. Erstelle eine Liste mit deinen drei Lieblingsfarben (als Strings).
    # 2. Wähle mit 'random.choice' eine zufällige Farbe aus und printe sie aus.
    # 3. Benutze eine for-Schleife mit 'enumerate', um alle Farben
    #    mit ihrem Index auszugeben.
    # 4. Wenn der Index 1 ist, überspringe ihn mit 'continue'.
    
    # ---> SCHREIBE DEINEN CODE HIER UNTER DIESER ZEILE:
    pass


# def: Definiert eine Funktion (Unterprogramm). 
# Das haben wir oben schon mehrfach gemacht!
def start_lernprogramm():
    print("=================================================")
    print("Willkommen zum Python-Kurs, Elias!")
    print("Gestalte deinen Code, löse die Aufgaben und teste sie!")
    print("=================================================")
    
    # Hier werden die Lektionen aufgerufen. 
    # Wenn du eine Aufgabe machst, führe die Datei aus, um zu testen!
    lektion_1_strings_und_punktnotation()
    lektion_2_listen_und_indizes()
    lektion_3_schleifen_und_random()
    
    print("\nSuper! Wenn du alle Aufgaben gelöst hast, bist du bereit für Hangman!")

# Das hier startet ganz zu Beginn unser Programm:
if __name__ == "__main__":
    start_lernprogramm()

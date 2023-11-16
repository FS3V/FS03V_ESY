# muenze_werfen.py

from random import randrange

def muenze_werfen(m):
    n = 1
    k = m

    print('\n         n       hn(Z)')
    print('_________________________')

    while n < m:
        z = 0
        n = 10 * n
        k = k / 10

        for i in range(1, n + 1):
            if randrange(1, 3) == 1:
                z = z + 1

        print((10 - len(str(n))) * ' ', n, '   ', float(z) / n)

# Hier wird die Funktion aufgerufen, wenn die Datei direkt ausgeführt wird
if __name__ == "__main__":
    anzahl_versuche = int(input("Anzahl der Versuche: "))
    muenze_werfen_anzahl_versuche(anzahl_versuche)

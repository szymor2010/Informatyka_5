import os

#wczytanie pliku z ocenami
with open("oceny.txt") as plik:
    oceny_str = plik.readline()

oceny = list(map(int, oceny_str.split(";")))

#wczytanie pliku z wagami
with open("wagi.txt") as plik:
    wagi_str = plik.readline()

wagi = list(map(int,wagi_str.split(";")))

suma = 0
suma_wag = 0

#obliczenia średniej ważonej
for o,w in zip(oceny, wagi):
    suma += o*w
    suma_wag += w

srednia = suma / suma_wag
print(srednia)
print("end.")

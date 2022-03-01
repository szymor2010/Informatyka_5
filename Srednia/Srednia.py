import os

with open("oceny.txt") as plik:
    oceny_str = plik.readline()

oceny = list(map(int, oceny_str.split(";")))

with open("wagi.txt") as plik:
    wagi_str = plik.readline()

wagi = list(map(int,wagi_str.split(";")))

suma = 0
suma_wag = 0

for o,w in zip(oceny, wagi):
    suma += o*w
    suma_wag += w

srednia = suma / suma_wag
print(srednia)
print("end.")

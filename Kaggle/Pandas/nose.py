import csv

with open("data.csv", "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    for fila in lector:
        print(fila)
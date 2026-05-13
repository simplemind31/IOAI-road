suma = 0

with open("datos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea)
        numero = int(linea.strip())
        suma += numero

print("Suma total:", suma)
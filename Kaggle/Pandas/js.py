import re

texto = "Edad: 18, Nota: 95"
m = re.search(r"Edad:\s*(\d+),\s*Nota:\s*(\d+)", texto)

if m:
    edad = int(m.group(1))
    nota = int(m.group(2))
print(edad,nota)
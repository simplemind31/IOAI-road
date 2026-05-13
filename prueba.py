def clasificar_puntaje(puntaje):
	if puntaje >= 85:
		return "Nivel alto"
	elif puntaje >= 60:
		return "Nivel medio"
	return "Nivel inicial"

nombre = input("Nombre del estudiante: ")
puntaje = int(input("Puntaje del examen: "))

nivel = clasificar_puntaje(puntaje)
print(f"{nombre} -> {nivel}")

with open("reporte.txt", "w", encoding="utf-8") as salida:
	salida.write(f"Estudiante: {nombre}\n")
	salida.write(f"Puntaje: {puntaje}\n")
	salida.write(f"Clasificacion: {nivel}\n")
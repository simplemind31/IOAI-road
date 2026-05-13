# Declaracion de variables
edad = 16              # int
altura = 1.72          # float
nombre = "Ana"         # str
es_estudiante = True   # bool

print(type(edad))          # <class 'int'>
print(type(altura))        # <class 'float'>
print(type(nombre))        # <class 'str'>
print(type(es_estudiante)) # <class 'bool'>

numero_texto = "42"
numero_int = int(numero_texto)        # str -> int
numero_float = float(numero_texto)    # str -> float

precio = 19.99
precio_entero = int(precio)           # float -> int (trunca decimales)

valor = 7
valor_str = str(valor)                # int -> str

print(numero_int, numero_float, precio_entero, valor_str)
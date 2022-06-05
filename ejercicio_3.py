# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

# Dado la siguiente lista de números, utilizar "for"
# para recorrer toda la lista y realizar la sumatoria de todos los números
# La sumatoria se deberá ir guardando en la variable "suma"
numeros = [1, 5, -1, 6, 10, 2, -5]
suma = 0   # Variable ya inicializada, la suma arranca en cero

for n in range(len(numeros)):
    suma = suma + numeros[n]

print("La sumatoria de la lista es", suma,".")

# Versión 2
suma = 0   # Para esta versión la variable suma es vuelta a cero

for n in numeros:
    suma = suma + n

print("La sumatoria de la lista es", suma,".")

print("¡Terminamos!, el resultado final almacenado en suma debe ser 18.")

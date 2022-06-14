# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y calcule la sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))
sumatoria = 0  # Inicializo el contador en 0

# En caso de que la secuencia sea creciente.
if inicio < fin:
    
    for t in range(inicio, fin + 1):
        sumatoria += t

# En caso que la secuencia sea decreciente.
elif inicio > fin:
    
    # for ... in range(....)
    for t in range(fin, inicio + 1):
        sumatoria += t

# El primer y el último elemento son iguales.
else:
    print("La secuencia tiene un solo elemento. La sumatoria es:", inicio,".")

# Imprimir el valor de la sumatoria
print("La sumatoria de los términos de la secuencia es:", sumatoria)

print("¡Terminamos!")

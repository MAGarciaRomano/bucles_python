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
# y cuente cuantos números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

secuencia = [inicio ,fin] # Se almacenan inicio y fin como elementos de una lista.

nuevos_terminos = abs(inicio - fin) - 1  # Se establece cuántos términos hay entre inicio y fin.

termino_agregado = inicio

# En caso de que la secuencia sea creciente.
if inicio < fin:
    
    for t in range(nuevos_terminos):
        posicion = t + 1
        termino_agregado = termino_agregado + 1
        secuencia.insert(posicion, termino_agregado)

    print("La secuencia es", secuencia)
    print("La secuencia tiene", len(secuencia), "elementos.")

# En caso que la secuencia sea decreciente.
elif inicio > fin:
    
    for t in range(nuevos_terminos):
        posicion = t + 1
        termino_agregado = termino_agregado - 1
        secuencia.insert(posicion, termino_agregado)

    print("La secuencia es", secuencia)
    print("La secuencia tiene". len(secuencia), "elementos.")

# El primer y el último elemento son iguales.
else:
    secuencia = [inicio]
    print("La secuencia tiene un solo elemento:", inicio)

cantidad_numeros_positivos = 0  # Inicializo el contador en 0


# for ... in range(....)
for elemento in range(len(secuencia)):
    if secuencia[elemento] >= 0:
        cantidad_numeros_positivos = cantidad_numeros_positivos + 1
    
cantidad_numeros_negativos = len(secuencia) - cantidad_numeros_positivos
    

# Imprimir el valor de la cantidad de números positivos y negativos
print("En la secuencia hay", cantidad_numeros_positivos, "elementos positivos o iguales a 0.")
print("En la secuencia hay", cantidad_numeros_negativos, "elementos negativos.")

print("¡Terminamos!")

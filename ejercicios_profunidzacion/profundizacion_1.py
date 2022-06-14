# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice un programa que pida por consola dos números que representen
el principio y fin de una secuencia numérica.
Realizar un bucle "for" que recorra esa secuencia armada con "range"
y cuente cuantos números ingresados hay, y la sumatoria de todos los números.
Al finalizar el bucle, utilice la variable "cantidad_numeros" y la variable
"sumatoria" para calcular el promedio de todos los números ingresados.
Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
sino que va hasta el anterior.
'''

print('Comenzamos a ponernos serios!')
# Empezar aquí la resolución del ejercicio

# inicio = ....
inicio = int(input('Ingrese el primer número de la secuencia:'))

# fin = ....
fin = int(input('Ingrese el último número de la secuencia:'))

# Creación de la secuencia de números como lista.

secuencia = [inicio , fin] # Inicialmente se almacenan inicio y fin como elementos de una lista.

nuevos_terminos = abs(inicio - fin) - 1  # Se establece cuántos términos hay entre inicio y fin.

# En caso de que la secuencia sea creciente.
if inicio < fin:
    
    for t in range(nuevos_terminos):
        posicion = t + 1
        termino_agregado = inicio + posicion
        secuencia.insert(posicion, termino_agregado)

# En caso que la secuencia sea decreciente.
elif inicio > fin:
    
    for t in range(nuevos_terminos):
        posicion = t + 1
        termino_agregado = inicio - posicion
        secuencia.insert(posicion, termino_agregado)

# En la secuencia el inicio y el fin son el mismo número. 
else:
    print("La secuencia tiene un solo elemento repetido:", inicio,".")

print(secuencia)

# cantidad_numeros ....
cantidad_numeros = 0

# sumatoria ....
sumatoria = 0

# bucle.....
for elemento in secuencia:
    cantidad_numeros += 1
    sumatoria = sumatoria + elemento

print('Cantidad de números en la secuencia numérica:', cantidad_numeros)
print('Sumatoria de los números de la secuencia numérica:', sumatoria)

# Al terminar el bucle calcular el promedio como:
# promedio = sumatoria / cantidad_numeros
promedio = sumatoria / cantidad_numeros

# Imprimir resultado en pantalla
print('Promedio de los números de la secuencia:', promedio)

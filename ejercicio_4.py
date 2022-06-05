# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

x = 0
# Realizar un bucle "while" cuya condición de continuidad
# sea que <x sea menor a 10> y que <x sea distinto de 6>
# Colocar ambas condiciones como condicion del "while" realizando
# una condición compuesta (utilice el operador "and" o "or" según corresponda)
# En cada iteracion del bucle debe incrementar el valor de "x" en "2"
# e imprimir en pantalla el resultado de X (antes de incrementar) con print
while x < 10 and x != 6:
    print("El valor de x es", x)
    x = x + 2

'''
Si el objetivo era mostrar los valores 0, 2, 4 y 8, el while con el doble condicional 
no funciona.

Si el operador es and, el while permite imprimir solamente los valores 0, 2 y 4.
El programa sale del bucle y deja de ejecutarse cuando x = 6.
Queda un valor sin mostrar que cumpliría la primera condición: 8.

Si el operador entre las condiciones es or, el programa entra en un bucle infinito
mostrando todos (infinitos) los valores posibles de x porque siempre al menos una de las dos
condiciones se va a cumplir.
Los primeros tres valores y el quinto valor (0, 2, 4 y 8) cumplirán las dos condiciones.
El tercer valor, 6, cumplirá la primera condición pero no la segunda condición.
A partir del sexto valor, 10, siempre se cumplirá la segunda condición.

Los resultados anteriores no cambian si se invierte el orden de las condiciones.
'''

# Realice el mismo bucle "while" pero en vez de estar formado por una condición
# compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
# "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
# En cada iteracion del bucle debe incrementar el valor de "x" en "2"
# e imprimir en pantalla el resultado de X (antes de incrementar) con print
while x < 10:
    if x == 6:
        pass
        
    else:
        print("El valor de x es", x)
       
    x = x + 2

print("terminamos!")

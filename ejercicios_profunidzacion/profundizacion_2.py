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
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''


print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

opcion = None

print('¿Qué operación desea realizar:')
print('Para suma pulse la tecla + ')
print('Para resta pulse la tecla - ')
print('Para multiplicación pulse la tecla * ')
print('Para división pulse / ')
print('Para potenciación escriba ** ')
print('Para salir escriba FIN')

while opcion != 'FIN':
    
    # Ingreso de los dos números para operar.
    primer_numero = float(input('Ingrese el primer número del cálculo:'))
    segundo_numero = float(input('Ingrese el segundo número del cálculo:'))

    # Selección de la operación a realizar, salida u error.
    opcion = str(input('¿Qué operación desea hacer?:')).upper()

    # Control de opción correcta, mensaje de error y reinicio del bucle.
    if (opcion != '+' and opcion != '-' and opcion != '*' and opcion != '/' and 
        opcion != '**' and opcion != 'FIN'):
        print('Error en la operación seleccionada.')
        continue
    
    # Cálculos e impresión de operación y resultados.
    elif opcion == '+':
        suma = primer_numero + segundo_numero
        print(f'{primer_numero} + {segundo_numero} = {suma}')

    elif opcion == '-':
        resta = primer_numero - segundo_numero
        print(f'{primer_numero} - {segundo_numero} = {resta}')

    elif opcion == '*':
        multiplicacion = primer_numero * segundo_numero
        print(f'{primer_numero} x {segundo_numero} = {multiplicacion}')

    elif opcion == '/':
        division = primer_numero / segundo_numero
        print(f'{primer_numero} / {segundo_numero} = {division}')

    elif opcion == '**':
        potenciacion = primer_numero ** segundo_numero
        print(f'{primer_numero} elevado a la {segundo_numero} = {potenciacion}')

    else:
        continue

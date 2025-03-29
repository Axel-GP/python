import random

lista = list(range(1, 101))  
aleatorio = random.choice(lista)  
nombre = input("Por favor, ingresa tu nombre: ")
numero = int(input(f'{nombre}, dime un número entre 1 y 100: '))
intentos = 0

while intentos < 9:
    if numero < 1 or numero > 100:
        print('El número no está permitido.')
    elif numero > aleatorio:
        print('El número que buscas es menor que el introducido.')
    elif numero < aleatorio:
        print('El número que buscas es mayor que el introducido.')
    else:
        print(f'¡Felicidades {nombre}! {aleatorio} es el número correcto.')
        break  
    intentos += 1
    numero = int(input(f'{nombre}, dime un número entre 1 y 100: '))

if intentos >= 9:
    print(f'Lo siento, {nombre}, se agotaron los intentos. El número correcto era {aleatorio}.')

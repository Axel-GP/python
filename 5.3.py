lista = list(range(1,101))
import random
aleatorio = random.randint(1,101)
nombre = input("Por favor, ingresa tu nombre: ")
numero = float(input(f'{nombre}, dime un número entre 1 y 100 '))
intentos = 0

while intentos < 9 :

    intentos += 1 

    numero = int(input(f'{nombre}, dime un número entre 1 y 100 '))

    if numero > 100 or numero < 1:
        print('El número no está permitido')

    elif numero > aleatorio:
        print('El número que buscas es menor que el introducido')
    
    elif numero < aleatorio:
        print('El número que buscas es mayor que el introducido')
    
    else:
        print(f'{aleatorio} es el número correcto')
    break
    
    


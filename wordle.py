import random

palabras_sin_tilde = [
    "abajo", "acero", "banco", "bardo", "barro", "basto", "canta", "canto", "carro", 
    "casas", "cerca", "cerro", "clavo", "colmo", "corte", "cosas", "cruce", "culpa", "denso", 
    "dicho", "dedos", "colar", "dosar", "duelo", "duras", "firme", "flota", "freno", "gasto", 
    "gente", "grito", "guapo", "lento", "lucha", "lomos", "macho", "manco", "manto", "molar", 
    "monto", "negro", "norte", "perro", "piano", "pinto", "pocas", "plaza", "plomo", "pobre", 
    "rango", "risas", "reino", "rojo", "roque", "silla", "sismo", "sordo", "tabla", "tinta", 
    "tinto", "turbo", "vapor", "vasto", "vello", "viola", "zorro", "tensa", "agota", "fiera", 
    "quema", "llama", "remar", "tango", "sueca", "cielo", "cita", "cavar", "madera", "largo", 
    "marca", "lamer", "soler", "suero", "roca", "circa", "letra", "manta", "rango", "pagar", 
    "lomos", "corta", "pinta", "serpa", "reves", "plana", "comas", "poros", "mismo", "calmo", 
    "sabro", "testar", "perco", "sumos", "gerbo", "lados", "cerca"
]

palabras_con_tilde = [
    "ratón", "limón", "árbol", "esquí", "mojón", "lápiz", "látex", "salón", "borró", "canté",
    "reptó", "móvil", "irías", "solía", "dócil", "dólar", "lucía", "moría", "vivía", "huías", "fácil"
]



eleccion = input("¿Quieres jugar con palabras con tildes o sin tildes? (escribe 'con' o 'sin'): ")


while eleccion not in ['con', 'sin']:
    eleccion = input("Por favor, elige 'con' o 'sin' para jugar con palabras con tildes o sin tildes: ")


if eleccion == 'con':
    palabras = palabras_con_tilde
else:
    palabras = palabras_sin_tilde


respuesta = random.choice(palabras)

print("Adivina la palabra de 5 letras.")
print("Funcionamiento de las pistas:")
print("Letra correcta en posición correcta: La letra")
print("Letra correcta en posición incorrecta: * ")
print("Letra incorrecta: _")
intentos = 6  

while intentos > 0:
    intento = input(f"Te quedan {intentos} intentos. Ingresa una palabra de 5 letras: ")
    
    if not len(intento) == 5:
        print("La palabra debe tener 5 letras. Inténtalo de nuevo.")
        continue

    
    if intento == respuesta:
        print(f"Adivinaste la palabra: {respuesta}")
        break

    
    resultado = ""
    for i in range(5):
        if intento[i] == respuesta[i]:
            resultado += intento[i]  
        elif intento[i] in respuesta:
            resultado += "*"  
        else:
            resultado += "_" 

    print("Pista:", resultado)
    intentos -= 1


if intentos == 0:
    print(f"Te quedaste sin intentos. La palabra correcta era: {respuesta}.")

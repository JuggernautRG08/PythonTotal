import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1: int, dado2: int) -> str:
    suma_dados = dado1 + dado2

    messages = {
        range(1, 7): f"La suma de tus dados es {suma_dados}. Lamentable",
        range(7, 10): f"La suma de tus dados es {suma_dados}. Tienes buenas chances",
        range(10, 13): f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    }

    for key in messages:
        if suma_dados in key:
            return messages[key]

# Ejemplo de uso
dado1, dado2 = lanzar_dados()
mensaje = evaluar_jugada(dado1, dado2)
print(mensaje)

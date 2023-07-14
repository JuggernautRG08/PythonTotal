def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()
print(next(g))
print(next(g))

print("Hola mundo")

print(next(g))


def perder_vida():
    vidas = 3
    while vidas > 0:
        yield "Te quedan {} vidas".format(vidas)
        vidas -= 1
    yield "Game Over"

# Ejemplo de uso del generador
perder_vida_gen = perder_vida()

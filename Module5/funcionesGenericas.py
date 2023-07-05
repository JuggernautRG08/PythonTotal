def suma(a, b):
    return a + b

print(suma(5,5))

def suma_args(*args):
    total= 0
    for arg in args:
        total += arg
    return total
print(suma_args(5,44,3,22,11,1))

def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje

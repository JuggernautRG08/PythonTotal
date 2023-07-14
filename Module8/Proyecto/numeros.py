def numero_perfumeria():
    for n in range(1, 1000000):
        yield f"P - {n}"

def numero_cosmetica():
    for n in range(1, 1000000):
        yield f"C - {n}"
def numero_farmacia():
    for n in range(1, 1000000):
        yield f"F - {n}"

p= numero_perfumeria()
c = numero_cosmetica()
f = numero_farmacia()

def decorador(rubro):
    print("\n" + "*" * 30)
    print("Su número es: ")
    if rubro == 'P':
        print(next(p))
    elif rubro == 'F':
        print(next(f))
    else:
        print(next(c))
    print("Espere su turno")
    print("\n" + "*" * 30)

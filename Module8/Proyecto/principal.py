import numeros

def preguntar():
    print("Bienvenido a farmacia Python")

    while True:
        print("[P] - Perfumeria [F] - Farmacia - [C] - Cosmetica")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Elija su rubro")
        else:
            break
        numeros.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Solicitar otro turno? [S] [N]: ").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print ("Opcion no valida")
        else:
            if otro_turno == 'N':
                print ("Gracias por su visita")
                break

inicio()

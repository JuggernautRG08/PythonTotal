class Persona():
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido,numero_cuenta,balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}. Balance de cuenta: {self.numero_cuenta}: ${self.balance}"

    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print ("Deposito aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")

def crear_cliente():
    nombre_cliente = input("Ingrese su nombre cliente: ")
    apellido_cliente = input("Ingrese su nombre apellido: ")
    numero_cuenta = input("Ingrese su número de cuenta: ")
    test_cliente= Cliente(nombre_cliente,apellido_cliente,numero_cuenta)
    return test_cliente

def inicio():
    mi_cliente=crear_cliente()
    print (mi_cliente)
    opcion=0
    while opcion != 'S':
        print(f'*'*25)
        print(f'-'*5 + 'Bienvenido al Banco de papel'+ '-'*5 )
        print(f'*'*25)
        print(f'-'*5 + 'Digite la letra para realizar una operación'+ '-'*5 )
        print(f'ELige: Depositar (D)')
        print(f'ELige: Retirar (R)')
        print(f'ELige: Salir (S)')
        opcion=input()
        if opcion == 'D':
            monto_dep=int(input("Ingrese la cantidad a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Ingrese la cantidad que desea retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)
    print(f'-'*5 + 'Gracias por operar en su banco de papel'+ '-'*5 )

inicio()

from random import randint
print('************Adivina el número************')
print('************************')
nombre=input("Ingresa el nombre del jugador: ")
print('************************')
intentos=0
secret_number = randint(1,100)
print('************************')
print("Piensa en un numero del 1 al 100\nTienes 8 intentos en total")
print('************************')
while intentos<8:
    numeroIngresado = int(input("Cual es tu número: "))
    intentos+=1

    if numeroIngresado not in (range(1,100)):
        print('************************')
        print ("El número ingresado debe estar dentro del rango de número del 1 al 100")
        print('************************')
    elif numeroIngresado>secret_number :
        print('************************')
        print (f"El número secreto es un número mas bajo. Te quedan {intentos - 8} intentos ")
        print('************************')
    elif numeroIngresado<secret_number:
        print('************************')
        print (f"El número secreto es un número mas alto. Te quedan {intentos - 8} intentos ")
        print('************************')
    elif numeroIngresado==secret_number:
        print('************************')
        print (f"¡Felicidades! - {nombre}, Adivinaste el número.")
        print('************************')
        break

if numeroIngresado != secret_number:
        print('************************')
        print (f"Agotaste los intentos, el número secreto era {secret_number}.")
        print('************************')

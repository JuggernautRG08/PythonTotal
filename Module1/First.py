my_list = ["a", "b", "c", "d", "e", "f"]
result = len(my_list)
print(result)
print(type(my_list))

#my_list[0] = "alfa"
my_list.append("g")
print(my_list)
my_list.pop()
print(my_list)


list_random =[1,240,300,4,8,11,33]
print(list_random)
list_random.sort()
print(list_random)

__dict__ = {'c1':1,'c2':2,'c3':3,'c4':4 }
__dict__[4]='c5'
print(__dict__)

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

t=(1,2,3,4,5,6,7,8,9,10)
print(t.count(1))

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")

print(sorteo)

var1 = True
var2 = False
print(type(var1))


# num1 = int(input("Ingresa un número:"))
# num2 = int(input("Ingresa otro número:"))
# if num1>num2:
#     print(f"{num1} es mayor que {num2}")
# elif num1<num2:
#     print(f"num2 es mayor que num1")
# else:
#     print(f"num1 y num2 son iguales")

lista =["ana","pedro","Roy","Anuel","Batman","Rodri","Hazard","Cole","Max","Maximo","Minimo","Medio","Full","Vacio","Complete","New"]
for nombre in lista:
    if nombre.startswith("M"):
        print(nombre)
    else:
        print("no se encontro coincidencia")

numbers=[1,2,3,4,5,6,7,8,9]
valors=0
for number in numbers:
    valors=valors+number
    print(valors)

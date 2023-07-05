class Animal():
     def __init__(self,edad,color):
         self.edad = edad
         self.color = color

     def nacer(self):
         print ("Nacio")

class Pajaro(Animal):
     pass

print(Pajaro)

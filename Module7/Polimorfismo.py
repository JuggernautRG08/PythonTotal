class Mago:
    def atacar(self):
        print("Ataque mágico")

class Arquero:
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai:
    def atacar(self):
        print("Ataque con katana")

class IteradorAtaqueConjugado:
    def __init__(self, personajes):
        self.personajes = personajes
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.personajes):
            raise StopIteration
        personaje = self.personajes[self.indice]
        self.indice += 1
        return personaje.atacar()


# Crear instancias de cada clase de personaje
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# Construir la lista de personajes
personajes = [arquero, mago, samurai]

# Crear el iterador y realizar el ataque conjugado
iterador = IteradorAtaqueConjugado(personajes)
for ataque in iterador:
    pass  # Hacer algo con cada ataque, en este caso simplemente pasar al siguiente


class Mago:
    def defender(self):
        print("Escudo mágico")

class Arquero:
    def defender(self):
        print("Esconderse")

class Samurai:
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()

# Ejemplo de uso
mago = Mago()
arquero = Arquero()
samurai = Samurai()

personaje_defender(mago)    # Salida: Escudo mágico
personaje_defender(arquero) # Salida: Esconderse
personaje_defender(samurai) # Salida: Bloqueo

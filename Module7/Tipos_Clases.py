class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
        print("Flecha lanzada. Cantidad de flechas restantes:", self.cantidad_flechas)


# Crear una instancia de Personaje con 5 flechas
personaje = Personaje(5)

# Lanzar una flecha
personaje.lanzar_flecha()  # Imprime: Flecha lanzada. Cantidad de flechas restantes: 4

# Lanzar otra flecha
personaje.lanzar_flecha()  # Imprime: Flecha lanzada. Cantidad de flechas restantes: 3

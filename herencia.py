from moduloT1 import Tamagotchi

class marutchi(Tamagotchi):
        def __init__(self, nombre, color, altura):
            super().__init__(nombre, color)
            self.altura= altura

        def jugar(self):
            print(self.nombre,"no esta muy contento de jugar")
            super().jugar()

class persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi= None

    def asignar_tamagotchi(self, tamagotchi):
        self.tamagotchi = tamagotchi
        return print(self.nombre,"ahora tiene un tamagotchi llamado",tamagotchi.nombre)

    def jugar_con_tamagotchi(self):
        if self.tamagotchi:
            self.tamagotchi.jugar()

    def darle_comida(self):
        if self.tamagotchi:
            self.tamagotchi.comer()

    def curarlo(self):
        if self.tamagotchi:
            self.tamagotchi.curar()

gala=marutchi("Gala","blanca","timida")
richard=persona("Richard","Marin")

richard.asignar_tamagotchi(gala)
richard.jugar_con_tamagotchi()
richard.darle_comida()
richard.curarlo()
richard.curarlo()
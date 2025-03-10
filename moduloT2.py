from moduloT1 import Tamagotchi

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

gala=Tamagotchi("Gala","blanca")
richard=persona("Richard","Marin")

richard.asignar_tamagotchi(gala)
richard.jugar_con_tamagotchi()
richard.darle_comida()
richard.curarlo()
richard.curarlo()
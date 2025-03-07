
class persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def jugar_con_tamagotchi(self):
        print("juegando con tamagotchi")
        gala.jugar()
        return 

    def darle_comida(self):
        print("alimentando a ", gala.nombre)

    def curarlo(self):
        print("dandole medicina a ",self.tamagotchinombre)

class Tamagotchi(persona):
    def __init__(self, nombre,apellido,tamagotchinombre,color,salud,felicidad,energia):
        super().__init__(nombre,apellido)
        self.tamagotchinombre=tamagotchinombre
        self.color=color
        self.salud= 100
        self.felicidad=100
        self.energia=100

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        return print (self.salud,self.felicidad)
    
    def comer(self):
        self.felicidad += 5
        self.salud -= 10
        return self
    
    def curar(self):
        self.salud += 20
        self.felicidad -=5

gala=Tamagotchi("richard","marin","gala","blanco",100,100,100)
richard=persona("richard","marin")


print(gala.nombre, gala.apellido,gala.tamagotchinombre,gala.felicidad)

richard.jugar_con_tamagotchi()
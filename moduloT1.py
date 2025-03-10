class Tamagotchi:
    def __init__(self,nombre,color):
        self.nombre=nombre
        self.color=color
        self.salud= 100
        self.felicidad=100
        self.energia=100

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        return print ("Jugaste con", self.nombre+", ahora su salud es",self.salud,"y su felicidad es",self.felicidad)
    
    def comer(self):
        self.felicidad += 5
        self.salud += 10
        return print ("Le diste de comer a ",self.nombre+", ahora su salud es",self.salud,
                    " y su felicidad es", self.felicidad)
    
    def curar(self):
        self.salud += 20
        self.felicidad -=5
        return print("Sanaste las heridas de tu tamagotchi, ahora su salud es", self.salud,"y su felicidad ahora es", self.felicidad)

    def __str__(self):
        return f"tamagotchi :{self.nombre}, color:{self.color}, salud:{self.salud},energia:{self.energia},felicidad:{self.felicidad}"


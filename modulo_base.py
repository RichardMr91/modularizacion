variable_base = "magia y arcoiris"

def area_rectangulo(base, altura):
    return base * altura

class Taco:
    def __init__(self, guiso):
        self.guiso = guiso

    def hacer_taco(self):
        return f"Hiciste un taquito de {self.guiso}"

print(variable_base)

taco_de_chicharron = Taco("chicharron")

print(taco_de_chicharron.guiso)
print(taco_de_chicharron.hacer_taco())




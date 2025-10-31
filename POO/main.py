class Carro:
    def __init__(self, motor = "", carroceria = "", volante = "", gasolina = 0, banco = 0, roda = 5):
        self.motor = motor
        lista_carrocerias = ["Fit", "City", "Civic"]
        if carroceria in lista_carrocerias:
            self.carroceria = carroceria
        self.roda = roda
        self.volante = volante
        self.gasolina = gasolina
        self.banco = banco
        self.ligado = False

    def ligar_carro(self):
        if self.ligado:
            print("O carro já está ligado")
        else:
            self.ligado = True
    
    def abastecer(self, litros: float):
        self.gasolina += litros

carro3 = Carro("1.4", "Fit", "Volante", 40, 5)

print (carro3.gasolina)
carro3.abastecer(50)

print(carro3.gasolina)
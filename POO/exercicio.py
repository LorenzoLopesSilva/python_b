
class TV:
    def __init__(self, marca: str, modelo: str, polegadas: float, tela: str, voltagem: int, canais: list, ligado: bool = False):
        self.marca = marca
        self.modelo = modelo
        self.polegadas = polegadas
        self.tela = tela
        self.voltagem = voltagem
        self.ligado = ligado
    
    def power(self):
        if self.ligado:
            print("A TV foi desligada")
            self.ligado = False
        else:
            print("A TV foi ligada")
            self.ligado = True
    
canaisSP = [
    (4, "Band"),
    (6, "Record"),
    (10, "TV Cultura"),
    (12, "Globo"),
    (30, "SBT")
]

tv_suprema = TV("Samsung", "STV8000 2025", 80.0, "UHD", 110, canaisSP)

tv_suprema.power()
tv_suprema.power()

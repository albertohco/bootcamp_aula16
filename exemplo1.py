class Veiculo:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor

    def descrever(self):
        return f"Um {self.tipo} de cor {self.cor}"


# Usando a abstração
carro = Veiculo("avião", "azul")
print(carro.descrever())

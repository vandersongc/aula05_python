class Carro:
    def __init__(self,nome,cor):
        self.nome = nome #atributo
        self.cor = cor #atributo
        self.velocidade = 0 #atributo inicial

    def acelerar(self):
        self.velocidade += 10
        print(f'{self.nome} está a {self.velocidade} km/h')

    def frear(self):
        self.velocidade -= 10
        print(f'{self.nome} reduzir para {self.velocidade} km/h')

carro1 = Carro('Fusca','Azul')
carro2 = Carro('Gol', 'Vermelho')
carro1.acelerar()
carro2.acelerar()
carro2.frear()

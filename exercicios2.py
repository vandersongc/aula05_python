'''
2. Crie uma classe Carro que tenha modelo, ano e velocidade.
Adicione métodos acelerar() e frear().
'''
print('='*50)
print('Atividade 2')
class Carro:
    def __init__(self,modelo, ano):
        self.modelo = modelo #atributo
        self.ano = ano #atributo
        self.velocidade = 0 #atributo inicial

    def acelerar(self):
        self.velocidade += 10
        print(f'{self.modelo} {self.ano} está a {self.velocidade} km/h')

    def frear(self):
        self.velocidade -= 10
        print(f'{self.modelo} {self.ano} reduzir para {self.velocidade} km/h')

carro1 = Carro('Fusca','1978')
carro2 = Carro('Gol', '2015')
carro1.acelerar()
carro2.acelerar()
carro2.frear()
print('='*50)

'''
1. Crie uma classe Pessoa com os atributos nome e idade.
Crie um método que exiba uma mensagem: “Olá, meu nome é [nome] e tenho [idade] anos.”
'''
print('='*50)
print('Atividade 1')
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def mensagem(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

pessoa1 = Pessoa('Ana','20')
pessoa1.mensagem()
print('='*50)


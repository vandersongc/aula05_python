'''




3. Crie uma classe Conta com saldo e métodos depositar() e sacar().

4. Crie uma classe Animal com método falar().

5. Crie uma classe Produto com atributos nome e preço. Crie um método desconto(percentual).

6. Crie uma classe Livro com título, autor e método exibir_detalhes().

7. Crie uma classe Aluno com nome, nota e método resultado() que diga se passou (nota ≥ 7).

8. Crie uma classe Calculadora com métodos somar, subtrair, multiplicar, dividir.

9. Crie uma classe Funcionario e uma classe Gerente que herda de Funcionario e adiciona o atributo setor.

10. Crie uma classe Retangulo com base e altura e método area().

Poder anexar tanto o arquivo.py  ou um link no github. Em ambos, deverá ter os comando das questões acima comentadas.

Boa sorte! 
'''

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

'''
3. Crie uma classe Conta com saldo e métodos depositar() e sacar().
'''
print('='*50)
print('Atividade 3')
class ContaBancaria:
    def __init__(self, saldo):
            self.__saldo = saldo #atributo privado

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        if valor <= self.__saldo:
            self.__saldo -=valor
        else:
            print('Saldo Insuficiente.')

    def mostrar_saldo(self):
        print(f'Saldo atual:R$ {self.__saldo}.')

contaBancaria1 = ContaBancaria('Itaú','Conta Corrente')
contaBancaria2 = ContaBancaria("Bradesco", "Poupança")
contaBancaria1.depositar()
contaBancaria1.depositar()
print('='*50)

'''
3. Crie uma classe Conta com saldo e métodos depositar() e sacar().
'''
print('='*50)
print('Atividade 3')
print('Saldo em conta: Bradesco')
class ContaBancaria:
    def __init__(self, banco, conta, saldo):
            self.banco = banco 
            self.conta = conta 
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

contaBancaria1 = ContaBancaria('Itaú','Conta Corrente', 40)
contaBancaria1.depositar()
contaBancaria1.depositar()
contaBancaria1.sacar()
print('='*50)

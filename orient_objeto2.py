class ContaBancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
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

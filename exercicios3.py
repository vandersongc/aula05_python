'''
3. Crie uma classe Conta com saldo e métodos depositar() e sacar().
'''
class ContaBancaria:
    def __init__(self, banco, conta, saldo):
        self.banco = banco
        self.conta = conta
        self.__saldo = saldo # atributo privado (bom uso do encapsulamento!)

    def depositar(self, valor):
        # Sempre verifique se o valor é positivo para depósitos
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado.')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f'Saque de R$ {valor:.2f} realizado.')
            else:
                print('Saldo Insuficiente.')
        else:
            print('Valor de saque inválido.')

    def mostrar_saldo(self):
        # Use :.2f para formatar como valor monetário com duas casas decimais
        print(f'Saldo atual: R$ {self.__saldo:.2f}')

print('='*50)
print('\nAtividade 3')
print('Saldo em conta: Bradesco')

contaBancaria1 = ContaBancaria('Itaú', 'Conta Corrente', 40.00) # Inicializado com 40.00
print(f"Conta criada. Banco: {contaBancaria1.banco}. Saldo inicial:")
contaBancaria1.mostrar_saldo()

# --- Chamadas Corrigidas (Passando o argumento 'valor') ---
print("\n--- Operações ---")
contaBancaria1.depositar(100.00)
contaBancaria1.depositar(5.50)
contaBancaria1.mostrar_saldo()

contaBancaria1.sacar(20.00)
contaBancaria1.mostrar_saldo()

# Tentando sacar um valor maior que o saldo (teste de erro)
contaBancaria1.sacar(500.00)
contaBancaria1.mostrar_saldo() # O saldo não deve mudar

print('='*50)

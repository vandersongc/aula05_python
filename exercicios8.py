'''
8. Crie uma classe Calculadora com métodos somar, subtrair, multiplicar, dividir.

'''
class Calculadora:
    """
    Uma classe que fornece métodos estáticos para realizar operações matemáticas básicas.
    
    Nota: Esta classe não precisa de atributos de instância, pois as operações
    dependem apenas dos números passados como argumentos.
    """
    
    # O método __init__ é opcional, mas podemos deixá-lo vazio se a classe for apenas para utilidade
    def __init__(self):
        # Não há atributos específicos para uma calculadora simples
        pass

    def somar(self, num1, num2):
        """
        Calcula a soma de dois números.

        Args:
            num1 (float/int): O primeiro número.
            num2 (float/int): O segundo número.

        Returns:
            float: A soma dos números.
        """
        return num1 + num2

    def subtrair(self, num1, num2):
        """
        Calcula a diferença entre dois números.

        Args:
            num1 (float/int): O primeiro número (minuendo).
            num2 (float/int): O segundo número (subtraendo).

        Returns:
            float: A diferença.
        """
        return num1 - num2

    def multiplicar(self, num1, num2):
        """
        Calcula o produto de dois números.

        Args:
            num1 (float/int): O primeiro número.
            num2 (float/int): O segundo número.

        Returns:
            float: O produto dos números.
        """
        return num1 * num2

    def dividir(self, num1, num2):
        """
        Calcula a divisão de dois números. Trata a divisão por zero.

        Args:
            num1 (float/int): O numerador (dividendo).
            num2 (float/int): O denominador (divisor).

        Returns:
            float or str: O resultado da divisão ou uma mensagem de erro.
        """
        if num2 == 0:
            return "Erro: Divisão por zero não é permitida."
        return num1 / num2

# --- Exemplos de Uso ---

print("="*50)
print("Atividade 8: Classe Calculadora")

# 1. Criando uma instância da Calculadora
calc = Calculadora()

# 2. Realizando operações
num_a = 15
num_b = 3

print(f"\nNúmeros usados: {num_a} e {num_b}")
print(f"Soma ({num_a} + {num_b}): {calc.somar(num_a, num_b)}")
print(f"Subtração ({num_a} - {num_b}): {calc.subtrair(num_a, num_b)}")
print(f"Multiplicação ({num_a} * {num_b}): {calc.multiplicar(num_a, num_b)}")
print(f"Divisão ({num_a} / {num_b}): {calc.dividir(num_a, num_b)}")

# 3. Testando divisão por zero
print(f"\nTeste de Divisão por Zero ({num_a} / 0): {calc.dividir(num_a, 0)}")

# 4. Usando números float
print(f"Soma de Floats (10.5 + 4.2): {calc.somar(10.5, 4.2)}")
print("="*50)
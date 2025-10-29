'''
10. Crie uma classe Retangulo com base e altura e método area().
'''

class Retangulo:
    """
    Representa uma forma geométrica retangular.
    """
    def __init__(self, base, altura):
        """
        Construtor da classe Retangulo.

        Args:
            base (float/int): O comprimento da base do retângulo.
            altura (float/int): A altura do retângulo.
        """
        # Garantindo que base e altura sejam números positivos
        if base <= 0 or altura <= 0:
            raise ValueError("Base e altura devem ser valores positivos.")
            
        self.base = base
        self.altura = altura

    def area(self):
        """
        Calcula a área do retângulo (base * altura).

        Returns:
            float: O valor da área.
        """
        return self.base * self.altura

    def perimetro(self):
        """
        Calcula o perímetro do retângulo (2 * (base + altura)).

        Returns:
            float: O valor do perímetro.
        """
        return 2 * (self.base + self.altura)

    def exibir_detalhes(self):
        """Exibe as dimensões e os cálculos do retângulo."""
        print("-" * 30)
        print(f"Retângulo de {self.base} x {self.altura}")
        print(f"Área Calculada: {self.area()}")
        print(f"Perímetro Calculado: {self.perimetro()}")
        print("-" * 30)


# --- Exemplos de Uso ---

print("="*50)
print("Atividade 10: Classe Retangulo")

# 1. Criando um objeto Retangulo
retangulo1 = Retangulo(base=10, altura=5)

# 2. Exibindo os cálculos
retangulo1.exibir_detalhes()

# 3. Criando um segundo objeto com valores float
retangulo2 = Retangulo(base=4.5, altura=7.2)
retangulo2.exibir_detalhes()

# 4. Tentando criar um retângulo inválido (Gera erro)
# try:
#     retangulo_invalido = Retangulo(base=-2, altura=5)
# except ValueError as e:
#     print(f"\nErro ao criar retângulo: {e}")

print("="*50)

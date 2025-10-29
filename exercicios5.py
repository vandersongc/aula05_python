'''
5. Crie uma classe Produto com atributos nome e preço. Crie um método desconto(percentual).

'''


class Produto:
    """
    Representa um produto com nome, preço e a capacidade de calcular um desconto.
    """
    def __init__(self, nome, preco):
        """
        Construtor da classe Produto.

        Args:
            nome (str): O nome do produto.
            preco (float): O preço original do produto.
        """
        self.nome = nome
        # O preço deve ser um número, idealmente float, para lidar com centavos
        self.preco = preco

    def desconto(self, percentual):
        """
        Calcula e retorna o novo preço do produto após aplicar um desconto.

        Args:
            percentual (int/float): O percentual de desconto a ser aplicado (ex: 10 para 10%).

        Returns:
            float: O novo preço com o desconto aplicado.
        """
        # Converte o percentual para um fator de multiplicação
        fator_desconto = 1 - (percentual / 100)
        
        # O novo preço é o preço original multiplicado pelo fator de desconto
        novo_preco = self.preco * fator_desconto
        
        # Retorna o preço com duas casas decimais
        return round(novo_preco, 2)

# --- Exemplos de Uso ---

print("="*50)
print("Atividade 5: Classe Produto")

# 1. Criando um objeto Produto
produto1 = Produto(nome="Notebook Gamer", preco=5000.00)

print(f"\nDetalhes do Produto: {produto1.nome}")
print(f"Preço Original: R$ {produto1.preco:.2f}")

# 2. Aplicando um desconto de 10%
percentual_desconto_1 = 10
preco_com_desconto_1 = produto1.desconto(percentual_desconto_1)

print(f"Desconto aplicado: {percentual_desconto_1}%")
print(f"Preço com Desconto: R$ {preco_com_desconto_1:.2f}")


# 3. Criando um segundo objeto e aplicando um desconto diferente
produto2 = Produto(nome="Mouse Sem Fio", preco=89.90)

percentual_desconto_2 = 25
preco_com_desconto_2 = produto2.desconto(percentual_desconto_2)

print(f"\nDetalhes do Produto: {produto2.nome}")
print(f"Preço Original: R$ {produto2.preco:.2f}")
print(f"Desconto aplicado: {percentual_desconto_2}%")
print(f"Preço com Desconto: R$ {preco_com_desconto_2:.2f}")
print("="*50)
'''
6. Crie uma classe Livro com título, autor e método exibir_detalhes().

'''
class Livro:
    """
    Representa um livro com seu título e autor.
    """
    def __init__(self, titulo, autor, ano_publicacao=None):
        """
        Construtor da classe Livro.

        Args:
            titulo (str): O título do livro.
            autor (str): O nome do autor do livro.
            ano_publicacao (int, optional): O ano em que o livro foi publicado.
        """
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_detalhes(self):
        """
        Método que imprime na tela todos os detalhes do livro.
        """
        print("--- Detalhes do Livro ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        
        # Condicionalmente exibe o ano, caso ele tenha sido fornecido
        if self.ano_publicacao:
            print(f"Ano de Publicação: {self.ano_publicacao}")
        else:
            print("Ano de Publicação: Não especificado")
        print("--------------------------")

# --- Exemplos de Uso ---

print("="*50)
print("Atividade 6: Classe Livro")

# 1. Criando um objeto Livro com todos os dados
livro1 = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", ano_publicacao=1954)

# 2. Chamando o método para exibir os detalhes
livro1.exibir_detalhes()

# 3. Criando um segundo objeto Livro sem o ano de publicação
livro2 = Livro(titulo="Cem Anos de Solidão", autor="Gabriel García Márquez")

# 4. Chamando o método para exibir os detalhes
livro2.exibir_detalhes()

print("="*50)
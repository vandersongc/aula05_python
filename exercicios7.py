'''
7. Crie uma classe Aluno com nome, nota e método resultado() que diga se passou (nota ≥ 7).
'''
class Aluno:
    """
    Representa um aluno com nome e nota, e um método para determinar sua situação
    (Aprovado ou Reprovado).
    """
    LIMITE_APROVACAO = 7.0  # Constante de classe para o limite de aprovação

    def __init__(self, nome, nota):
        """
        Construtor da classe Aluno.

        Args:
            nome (str): O nome completo do aluno.
            nota (float): A nota final do aluno (de 0.0 a 10.0).
        """
        self.nome = nome
        self.nota = nota

    def resultado(self):
        """
        Verifica a nota do aluno e retorna uma string indicando se ele está
        'Aprovado' ou 'Reprovado'.

        Returns:
            str: "Aprovado" ou "Reprovado".
        """
        if self.nota >= self.LIMITE_APROVACAO:
            return "Aprovado"
        else:
            return "Reprovado"

    def exibir_status(self):
        """
        Exibe na tela o nome do aluno, sua nota e o resultado.
        """
        status = self.resultado()
        print(f"Aluno: {self.nome}")
        print(f"Nota Final: {self.nota:.1f}")
        print(f"Resultado: **{status}**")
        print("-" * 20)


# --- Exemplos de Uso ---

print("="*50)
print("Atividade 7: Classe Aluno")

# 1. Criando um aluno APROVADO
aluno1 = Aluno(nome="Maria Silva", nota=8.5)
aluno1.exibir_status()

# 2. Criando um aluno REPROVADO
aluno2 = Aluno(nome="João Santos", nota=6.9)
aluno2.exibir_status()

# 3. Criando um aluno na linha de corte
aluno3 = Aluno(nome="Pedro Alves", nota=7.0)
aluno3.exibir_status()

print("Limite de Aprovação Usado: ", Aluno.LIMITE_APROVACAO)
print("="*50)
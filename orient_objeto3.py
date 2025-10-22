
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self,nome,idade,matricula):
        super().__init__(nome,idade)
        self.matricula = matricula

aluno1 = Aluno('Maria','20','A123')
print(aluno1.nome)
print(aluno1.matricula)


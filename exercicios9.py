'''
9. Crie uma classe Funcionario e uma classe Gerente que herda de Funcionario e adiciona o atributo setor.
 
'''
class Funcionario:
    """
    Classe base para representar um funcionário genérico.
    Possui atributos básicos que todos os funcionários compartilham.
    """
    def __init__(self, nome, cargo, salario):
        """
        Construtor da classe Funcionario.

        Args:
            nome (str): O nome do funcionário.
            cargo (str): O cargo atual do funcionário.
            salario (float): O salário mensal do funcionário.
        """
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_info(self):
        """Exibe as informações básicas do funcionário."""
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario:,.2f}") # Formatação para moeda


class Gerente(Funcionario):
    """
    Subclasse que herda de Funcionario e adiciona o atributo 'setor'.
    """
    def __init__(self, nome, salario, setor):
        """
        Construtor da classe Gerente.

        Chama o construtor da classe pai (Funcionario) e adiciona o 'setor'.

        Args:
            nome (str): O nome do gerente.
            salario (float): O salário mensal do gerente.
            setor (str): O setor que o gerente administra.
        """
        # 1. Chamada ao construtor da classe pai (Funcionario) usando super()
        # O cargo é definido como 'Gerente' automaticamente.
        super().__init__(nome, "Gerente", salario) 
        
        # 2. Inicialização do novo atributo específico da subclasse
        self.setor = setor

    def exibir_info(self):
        """Sobrescreve o método da classe pai para incluir o setor."""
        # Chamada ao método exibir_info da classe pai para reuso do código
        super().exibir_info()
        print(f"Setor Administrado: {self.setor}")


# --- Exemplos de Uso ---

print("="*50)
print("Atividade 9: Herança Funcionario/Gerente")

# 1. Criando um objeto Funcionario (Classe Pai)
print("\n--- Informações do Funcionário (Classe Pai) ---")
func1 = Funcionario(nome="Ana Costa", cargo="Analista de Dados Júnior", salario=3500.00)
func1.exibir_info()

# 2. Criando um objeto Gerente (Classe Filha)
print("\n--- Informações do Gerente (Classe Filha) ---")
gerente1 = Gerente(nome="Bruno Ferreira", salario=8500.00, setor="Tecnologia")
gerente1.exibir_info()

print("="*50)
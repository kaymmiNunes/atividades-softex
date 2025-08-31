# Registros de alunos com as 3 notas e situação de aprovação

alunos = []  # lista para armazenar todos os alunos cadastrados

# Função para cadastrar um aluno
def cadastro():
    nome = input("\nDigite o nome do aluno: ")  # solicita o nome
    try:
        idade = int(input("\nDigite a idade do aluno: "))  # solicita idade
    except ValueError: 
        print("\n⚠ Idade inválida! Tente novamente")
        return
    
    # Cria dicionário com dados do aluno
    aluno =  {
        "nome": nome,
        "idade": idade,
        "notas": [],
        "aprovado": False  # inicializa como reprovado
    }  
    
    for i in range(3):  # cadastra 3 notas
        try:
            nota = float(input(f"\nDigite a nota {i+1} do aluno: "))
            aluno["notas"].append(nota)
        except ValueError:
            print("\n⚠ Nota inválida! Tente novamente")

    print(f"\n✅ Aluno {nome} cadastrado com sucesso!\n")

    media = sum(aluno["notas"]) / len(aluno["notas"])  # calcula média

    # Define aprovação
    aluno["aprovado"] = media >= 7
    
    alunos.append(aluno)  # adiciona aluno à lista

# Função para exibir todos os alunos cadastrados
def ver_registro():
    if not alunos:
        print("\n⚠ Nenhum registro encontrado.")
        return
    
    print("\n📋 Lista de alunos cadastrados:")
    for i, aluno in enumerate(alunos, start=1):
        print(f"\nAluno {i}:")
        print(f"  Nome: {aluno['nome']}")
        print(f"  Idade: {aluno['idade']} anos")
        print(f"  Notas: {aluno['notas']}")
        print(f"  Aprovado: {aluno['aprovado']}")

# Menu principal
def menu():
    while True:
        print("\n____ Menu de opções ____")
        print("\nDigite 1 para registrar alunos")
        print("Digite 2 para visualizar os registros")
        print("Digite 3 para sair")
        opcao = input("\nDigite a opção: ")

        if opcao == "1":
            cadastro()
        elif opcao == "2":
            ver_registro()
        elif opcao == "3":
            print("\nEncerrando...")
            break
        else:
            print("\n⚠ Opção inválida!")

# Executa o menu apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    menu()

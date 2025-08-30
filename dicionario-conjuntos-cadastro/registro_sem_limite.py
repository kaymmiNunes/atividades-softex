## Registros de alunos com as 3 notas e situação de aprovação

alunos = [] # Lista vazia para armazenar todos os alunos cadastrados

# Função para cadastrar um aluno
def cadastro():
    nome = input("\nDigite o nome do aluno: ") # Solicita o nome do aluno
    try:
        idade = int(input("\nDigite a idade do aluno: ")) # Solicita a idade e converte para inteiro
    except ValueError: 
        print("\n⚠ Idade inválida! Tente novamente") # Caso a entrada não seja um número inteiro
        return
    
    # Cria um dicionário para armazenar os dados do aluno
    aluno =  {
        "nome": nome,          # Nome do aluno
        "idade": idade,        # Idade do aluno
        "notas": [],           # Lista para armazenar notas
        "aprovado": False      # Situação inicial como reprovado
    }  
    
    for i in range(3): # Loop para cadastrar 3 notas
        try:
            nota = float(input(f"\nDigite a nota {i+1} do aluno: ")) # Solicita a nota e converte para float
            aluno["notas"].append(nota) # Adiciona a nota na lista de notas
        except ValueError: # Caso a nota não seja número válido
            print("\n⚠ Nota inválida! Tente novamente")

    print(f"\n✅ Aluno {nome} cadastrado com sucesso!\n") # Mensagem de confirmação de cadastro

    media = sum(aluno["notas"]) / len(aluno["notas"]) # Calcula a média das notas

    if media >= 7: # Verifica se a média é maior ou igual a 7
        aluno["aprovado"] = True
    else:
        aluno["aprovado"] = False
    
    alunos.append(aluno) # Adiciona o aluno na lista de alunos

# Função para exibir todos os alunos cadastrados
def ver_registro():
    if not alunos: # Se a lista de alunos estiver vazia
        print("\n⚠ Nenhum registro encontrado.")
        return
    
    print("\n📋 Lista de alunos cadastrados:") # Exibe todos os alunos da lista
    for i, aluno in enumerate(alunos, start=1):  # enumera os alunos a partir de 1
        print(f"\nAluno {i}:")
        print(f"  Nome: {aluno['nome']}")        # Mostra o nome
        print(f"  Idade: {aluno['idade']} anos") # Mostra a idade
        print(f"  Notas: {aluno['notas']}")      # Mostra as notas
        print(f"  Aprovado: {aluno['aprovado']}")# Mostra se foi aprovado ou não

# Função principal que exibe o menu de opções
def menu():
    while True:  # Loop infinito até o usuário escolher sair
        print("\n____ Menu de opcões ____")
        print("\nDigite 1 para registrar alunos ")
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
        # Se não for nenhuma das opções acima
        else:
            print("\n⚠ Opção inválida!")

# Garante que o menu só será executado se o arquivo for rodado diretamente
if __name__ == "__main__":
    menu()
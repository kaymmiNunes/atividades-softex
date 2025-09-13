# Sistema simples de cadastro de alunos e notas

alunos = {}

def cadastro():
    nome_aluno = input("Digite o nome do aluno: ")
    disciplina = input("Digite a disciplina: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    alunos[nome_aluno, disciplina] = (nota1, nota2, nota3)
    print(f"Aluno {nome_aluno} cadastrado com sucesso!\n")

def ver_notas():
    pesquisa = input("Digite o nome do aluno para ver suas notas: ")
    encontrado = False
    for (nome, disciplina), notas in alunos.items():
        if nome.lower() == pesquisa.lower():  # busca sem diferenciar maiúsculas/minúsculas
            media = sum(notas) / len(notas)
            print(f"Aluno: {nome} | Disciplina: {disciplina} | Notas: {notas} | Média: {media:.2f}")
            encontrado = True
    if not encontrado:
        print("Aluno não encontrado.\n")

def menu():
    while True:
        print("\n1 - Cadastrar aluno")
        print("2 - Ver notas do aluno")
        print("3 - Sair")
        usuario = input("Opção: ")

        if usuario == "1":
            cadastro()
        elif usuario == "2":
            ver_notas()
        elif usuario == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.\n")

menu()

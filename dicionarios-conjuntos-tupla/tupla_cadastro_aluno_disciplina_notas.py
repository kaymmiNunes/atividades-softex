alunos = {}


def cadastro():
    nome_aluno = input("Digite o nome do aluno: ")
    disciplina = input("Digite a disciplina: ")
    nota1 = float(input("Digite a nota: "))
    nota2 = float(input("Digite a nota: "))
    nota3 = float(input("Digite a nota: "))

    alunos[nome_aluno, disciplina] = (nota1, nota2, nota3)

def ver_notas():
    for (nome, disciplina), notas in alunos.items():
        pesquisa = input("Digite o nome do aluno para ver suas notas: ")
        alunos.get(pesquisa)
        for (nome, disciplina), notas in alunos.items():
            if nome == pesquisa:
                media = sum(notas) / len(notas)
                print(f"Aluno: {nome} | Disciplina: {disciplina} | Notas: {notas} | Média: {media:.2f}")

def menu():
    while True:
        print("1 - Cadastrar aluno")
        print("2 - Ver notas do aluno")
        print("3 - Sair")

        usuario = input("Opção: ")

        if usuario == "1":
            cadastro()
        elif usuario == "2":
            ver_notas()
        elif usuario == "3":
            exit()
        else:
            print("Opção inválida, tente novamente.")
            menu()

menu()
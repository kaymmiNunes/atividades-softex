# Sistema de cadastro e pesquisa de alunos

alunos = {}  # chave: (nome, disciplina), valor: nota

def menu():
    while True:
        print("1 - Adicionar aluno")
        print("2 - Pesquisar aluno")
        print("3 - Sair")

        usuario = input("Opção: ")

        if usuario == "1":
            adicionar()
        elif usuario == "2":
            pesquisar()
        elif usuario == "3":
            sair()
        else:
            print("Opção inválida, tente novamente.")

def adicionar():
    try:
        nome_aluno = input("Nome do aluno: ")
        disciplina = input("Disciplina: ")
        nota = float(input("Nota: "))
        alunos[nome_aluno, disciplina] = nota  # armazena nota associada a aluno e disciplina
    except ValueError:
        print("Valor inválido, tente novamente.")

def pesquisar():
    p_aluno = input("Nome do aluno: ")
    encontrado = False
    for (nome, disciplina), nota in alunos.items():
        if nome.lower() == p_aluno.lower():  # busca sem diferenciar maiúsculas/minúsculas
            print(f"Disciplina: {disciplina} - Nota: {nota}")
            encontrado = True
    if not encontrado:
        print("Aluno não encontrado.")

def sair():
    print("Saindo...")
    exit()
    
menu()

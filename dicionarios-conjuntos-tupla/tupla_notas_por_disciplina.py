alunos = {}

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
                menu()
        
def adicionar():
    try:
        nome_aluno = input("Nome do aluno: ")
        disciplina = input("Disciplina: ")
        nota = float(input("Nota: "))

        alunos[nome_aluno, disciplina] = nota
    except ValueError:
        print("Valor inválido, tente novamente.")
        menu()

def pesquisar():
    p_aluno = input("Nome do aluno: ")
    alunos.get(p_aluno)
    for (nome, disciplina), nota in alunos.items():
        if nome == p_aluno:
            print(f"Disciplina: {disciplina} - Nota: {nota}")

    
def sair():
        print("Saindo...")
        exit()
    
menu()
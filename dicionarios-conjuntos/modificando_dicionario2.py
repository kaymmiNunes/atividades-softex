# Registros de alunos com 3 notas e situação de aprovação

alunos = []

def cadastro():
    nome = input("\nDigite o nome do aluno: ")
    try:
        idade = int(input("\nDigite a idade do aluno: "))
    except ValueError: 
        print("\n⚠ Idade inválida! Tente novamente")
        return
    
    aluno =  {
    "nome": nome,
    "idade": idade, 
    "notas": [],
    "aprovado": False}  
    
    for i in range(3):
        try:
            nota = float(input(f"\nDigite a nota {i+1} do aluno: "))
            aluno["notas"].append(nota)
        except ValueError:
            print("\n⚠ Nota inválida! Tente novamente")

    print(f"\n✅ Aluno {nome} cadastrado com sucesso!\n")

    media = sum(aluno["notas"]) / len(aluno["notas"])
    if media >= 7:
        aluno["aprovado"] = True
    else:
        aluno["aprovado"] = False

    alunos.append(aluno)

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

def menu():
    while True:
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
        else:
            print("\n⚠ Opção inválida!")

if __name__ == "__main__":
    menu()







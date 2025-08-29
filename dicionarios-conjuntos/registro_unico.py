# Registro de aluno com nota e aprovação

aluno = {
    "nome": "Desconhecido",
    "idade": 0, 
    "nota": 0,
    "aprovado": False
}

print("==== Registro do aluno ====")
aluno["nome"] = input("Digite o nome do aluno: ")
aluno["idade"] = int(input("Digite a idade do aluno: "))
aluno["nota"] = float(input("Digite a nota do aluno: "))

if aluno["nota"] >= 7:
    aluno["aprovado"] = True
else:
    aluno["aprovado"] = False

print(f'O aluno {aluno["nome"]} de {aluno["idade"]} anos com a nota {aluno["nota"]} está {"aprovado" if  aluno["aprovado"] == True else "reprovado"}')






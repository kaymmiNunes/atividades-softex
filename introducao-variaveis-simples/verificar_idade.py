# Verificar se o usuário é maior de idade

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
mairDeIdade = idade

print(f"Seu nome é {nome}, você tem {idade} anos e mede {altura}")

if idade >= 18: 
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
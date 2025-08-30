# Verificador de senha “forte”

senha = input("Digite sua senha para a análise: ")

if len(senha) >= 8:
    print("Tem 8 ou mais caracteres")
else:
    print("Precisa ter 8 ou mais caracteres")

if any(c.islower() for c in senha):
    print("Possui pelo menos 1 caractere em minúsculo")
else:
    print("Precisa de pelo menos 1 caractere em minúsculo")

if any(c.isupper() for c in senha):
    print("Possui pelo menos 1 caractere em maiúsculo")
else:
    print("Precisa de pelo menos 1 caractere em maiúsculo")

if any(c.isdigit() for c in senha):
    print("Possui pelo menos 1 número")
else:
    print("Precisa de pelo menos 1 número")


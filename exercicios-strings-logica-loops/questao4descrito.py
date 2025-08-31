# Verificador de senha “forte” (mostra cada critério)

senha = input("Digite sua senha para a análise: ")

# Verifica comprimento
if len(senha) >= 8:
    print("Tem 8 ou mais caracteres")
else:
    print("Precisa ter 8 ou mais caracteres")

# Verifica minúsculas
if any(c.islower() for c in senha):
    print("Possui pelo menos 1 caractere em minúsculo")
else:
    print("Precisa de pelo menos 1 caractere em minúsculo")

# Verifica maiúsculas
if any(c.isupper() for c in senha):
    print("Possui pelo menos 1 caractere em maiúsculo")
else:
    print("Precisa de pelo menos 1 caractere em maiúsculo")

# Verifica números
if any(c.isdigit() for c in senha):
    print("Possui pelo menos 1 número")
else:
    print("Precisa de pelo menos 1 número")

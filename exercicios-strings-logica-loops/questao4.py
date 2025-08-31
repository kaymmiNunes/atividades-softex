# Verificador de senha “forte”

senha = input("Digite sua senha para a análise: ")

# Verifica critérios de senha forte
if (len(senha) >= 8 and
    any(c.islower() for c in senha) and
    any(c.isupper() for c in senha) and
    any(c.isdigit() for c in senha)):
    print("✅ A senha é forte")
else:
    print("❌ Senha inválida! Deve ter pelo menos 8 caracteres, 1 maiúscula, 1 minúscula e 1 número.")

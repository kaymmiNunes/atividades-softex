# Verificador de senha “forte”

senha = input("Digite sua senha para a análise: ")  # entrada da senha do usuário

if (len(senha) >= 8 and  # verifica se a senha tem pelo menos 8 caracteres
    any(c.islower() for c in senha) and  # verifica se existe pelo menos uma letra minúscula
    any(c.isupper() for c in senha) and  # verifica se existe pelo menos uma letra maiúscula
    any(c.isdigit() for c in senha)):  # verifica se existe pelo menos um número
    print("✅ A senha é forte")  # imprime mensagem se todas as condições forem verdadeiras
else:
    print("❌ Senha inválida! Deve ter pelo menos 8 caracteres, 1 maiúscula, 1 minúscula e 1 número.") 


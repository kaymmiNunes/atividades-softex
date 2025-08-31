# Dicionário com preços de produtos e seus tamanhos
precos = {
    ("Camiseta", "M"): 35,
    ("Camiseta", "G"): 40,
    ("Camiseta", "p"): 55,
    ("Calça", "M"): 120
}

# Percorre cada item do dicionário
for (produto, tamanho), preco in precos.items():
    pesquisa = input("Digite o nome do produto ou Tamanho: ")  # recebe entrada do usuário

    precos.get(pesquisa)  # tenta acessar valor (não é usado depois)
    # Percorre novamente para comparar produto ou tamanho
    for (produto, tamanho), preco in precos.items():
        if produto == pesquisa or tamanho == pesquisa:  # verifica se o produto ou tamanho corresponde à pesquisa
            print(f"Produto: {produto} | Tamanho: {tamanho} | Preço: R$ {preco}")  # exibe resultado
if corrigir!!!!
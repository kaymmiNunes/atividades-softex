precos = {
    ("Camiseta", "M"): 35,
    ("Camiseta", "G"): 40,
    ("Camiseta", "p"): 55,
    ("Calça", "M"): 120
}

for (produto, tamanho), preco in precos.items():
    pesquisa = input("Digite o nome do produto ou Tamanho: ")

    precos.get(pesquisa)
    for (produto, tamanho), preco in precos.items():
            if produto == pesquisa or tamanho == pesquisa:
                print(f"Produto: {produto} | Tamanho: {tamanho} | Preço: R$ {preco}")


                
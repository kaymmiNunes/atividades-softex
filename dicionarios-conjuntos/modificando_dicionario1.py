# Cadastro de produtos e valor total

produto = {
    "nome": "Desconhecido",
    "preço": 0, 
    "quantidade": 0,
    "total": 0
}

print("==== Registro do produto ====")
produto["nome"] = input("Digite o nome do produto: ")
produto["preço"] = float(input("Digite o preço: "))
produto["quantidade"] = int(input("Digite a quantidade: "))

produto["total"] = produto["preço"] * produto["quantidade"]

print(f'Nome do produto: {produto["nome"]} | Preço: R$ {produto["preço"]} | Quantidade: {produto["quantidade"]} | Total: R$  {produto["total"]}')
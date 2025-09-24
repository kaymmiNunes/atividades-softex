#1. Listas: Crie uma lista com os números de 1 a 5 e imprima cada elemento.
print("\n1. Listas: Crie uma lista com os números de 1 a 5 e imprima cada elemento.\n")

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

#2. Condicionais: Peça um número ao usuário e verifique se é positivo, negativo ou zero.
print("\n2. Condicionais: Peça um número ao usuário e verifique se é positivo, negativo ou zero.\n")
try:
    numero = float(input("Digite um número: "))
    if numero >= 0:
        print(f"O número {numero} é positivo.")
    else: 
        print(f"O número {numero} é negativo.")
except:
    print("Provavelmente você escreveu uma letra ou símbolo. \
          Rode o programa novamente e digite um número.")

#3. Laços: Use um loop for para imprimir os números de 1 a 10.
print("\n3. Laços: Use um loop for para imprimir os números de 1 a 10.\n")

for i in range(1, 11):
    print(i)

#4. Dicionários: Crie um dicionário com nomes e idades de 3 pessoas e imprima cada par.
print("\n4. Dicionários: Crie um dicionário com nomes e idades de 3 pessoas e imprima cada par.\n")

pessoas = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}

for nome, idade in pessoas.items():
    print(f"{nome} tem {idade} anos.")

#5. Funções: Crie uma função que recebe dois números e retorna a soma.
print("\n5. Funções: Crie uma função que recebe dois números e retorna a soma.\n")

def soma(a, b):
    return a + b

numero1 = float(input("Digite o primeiro número: ")) 
numero2 = float(input("Digite o segundo número: "))
resultado = soma(numero1, numero2)
print(f"A soma de {numero1} e {numero2} é {resultado}.")

#6. Strings: Peça uma palavra ao usuário e imprima o número de caracteres.
print("\n6. Strings: Peça uma palavra ao usuário e imprima o número de caracteres.\n")

letras = []
palavra = input("Digite uma palavra: ")
for letra in palavra:
    letras.append(letra)
    quantidade = len(letras)

print(f"A palavra '{palavra}' tem {quantidade} letras.")

#7. **Listas**: Crie uma lista com 3 frutas e adicione uma nova fruta.
print("\n7. Listas: Crie uma lista com 3 frutas e adicione uma nova fruta.\n")

frutas = ["maçã", "banana", "laranja"]
fruta_nova = input("Digite o nome de uma nova fruta: ")
frutas.append(fruta_nova)
print("Lista de frutas atualizada:", frutas)

#8. **Condicionais**: Peça a idade do usuário e verifique se ele é maior de idade.
print("\n8. Condicionais: Peça a idade do usuário e verifique se ele é maior de idade.\n")
try:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
except:
    print("Provavelmente você escreveu uma letra ou símbolo. \
          Rode o programa novamente e digite um número.")   

#9. **Laços**: Use um loop while para imprimir os números de 1 a 5.
print("\n9. Laços: Use um loop while para imprimir os números de 1 a 5.\n")
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
# OU 
print("\nOutra forma de fazer usando for:\n")

for i in range(1, 6):
    print(i)

#10. **Dicionários**: Crie um dicionário com 3 países e suas capitais e imprima cada par.
print("\n10. Dicionários: Crie um dicionário com 3 países e suas capitais e imprima cada par.\n")
paises = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "Colômbia": "Bogotá"
}

for pais, capital in paises.items():
    print(f"A capital do {pais} é {capital}.")

#11. **Listas + Laços**: Crie uma lista de números e calcule a soma de todos os elementos.
print("\n11. Listas + Laços: Crie uma lista de números e calcule a soma de todos os elementos.\n")
numeros = [1, 2, 3, 4, 5]
soma = 0

for numero in numeros:
    soma += numero
print("A soma dos números na lista é:", soma)

#12. **Dicionários com Tuplas**: Crie um dicionário onde cada chave é um nome e o valor é uma tupla com (idade, cidade).
print("\n12. Dicionários com Tuplas: Crie um dicionário onde cada chave é um nome e o valor é uma tupla com (idade, cidade).\n")
pessoas = {
    "Alice": (30, "São Paulo"),
    "Bob": (25, "Rio de Janeiro"),
    "Charlie": (35, "Belo Horizonte")
}

for nome, (idade, cidade) in pessoas.items():
    print(f"{nome} tem {idade} anos e mora em {cidade}.")

#13. **Condicionais Aninhadas**: Classifique um número como "pequeno" (<10), "médio" (10-50) ou "grande" (>50).
print("\n13. Condicionais Aninhadas: Classifique um número como 'pequeno' (<10), 'médio' (10-50) ou 'grande' (>50).\n")
try:
    numero = float(input("Digite um número: "))
    if numero < 10:
        print(f"O número {numero} é pequeno.")
    elif 10 <= numero <= 50:
        print(f"O número {numero} é médio.")
    else:
        print(f"O número {numero} é grande.")
except:
    print("Provavelmente você escreveu uma letra ou símbolo. \
          Rode o programa novamente e digite um número.")

#14. **Laços Aninhados**: Imprima uma tabuada de 1 a 5 (ex: 1x1=1, 1x2=2, etc.).
print("\n14. Laços Aninhados: Imprima uma tabuada de 1 a 5 (ex: 1x1=1, 1x2=2, etc.).\n")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Linha em branco entre as tabuadas

#15. **Funções + Listas**: Crie uma função que recebe uma lista e retorna o maior número.
print("\n15. Funções + Listas: Crie uma função que recebe uma lista e retorna o maior número.\n")
def maior_numero(lista):
    if not lista:
        return None
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

numeros = [3, 5, 2, 8, 1]
print("Lista de números:", numeros)
print("O maior número na lista é:", maior_numero(numeros))

#16. **Dicionários**: Conte a frequência de cada letra em uma palavra (ex: "hello" → {'h':1, 'e':1, 'l':2, 'o':1}).
print("\n16. Dicionários: Conte a frequência de cada letra em uma palavra (ex: 'hello' → {'h':1, 'e':1, 'l':2, 'o':1}).\n")
palavra = input("Digite uma palavra: ")
frequencia = {}
for letra in palavra:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1
print("Frequência das letras:", frequencia)

#17. **Listas de Dicionários**: Crie uma lista de dicionários representando livros (título, autor, ano) e imprima todos.
print("\n17. Listas de Dicionários: Crie uma lista de dicionários representando livros (título, autor, ano) e imprima todos.\n")
livros = [
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949},
    {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899}
]
for livro in livros:
    print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")

#18. **Condicionais + Strings**: Verifique se uma string é um palíndromo (ex: "radar").
print("\n18. Condicionais + Strings: Verifique se uma string é um palíndromo (ex: 'radar').\n")
def eh_palindromo(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
palavra = input("Digite uma palavra: ")
if eh_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

#19. **Laços + Condicionais**: Imprima apenas os números pares entre 1 e 20.
print("\n19. Laços + Condicionais: Imprima apenas os números pares entre 1 e 20.\n")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#20. **Funções Recursivas**: Crie uma função recursiva para calcular o fatorial de um número.
print("\n20. Funções Recursivas: Crie uma função recursiva para calcular o fatorial de um número.\n")
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é {fatorial(numero)}.")

#21. **Listas + Dicionários**: Transforme duas listas (uma de chaves, outra de valores) em um dicionário.
print("\n21. Listas + Dicionários: Transforme duas listas (uma de chaves, outra de valores) em um dicionário.\n")
chaves = ["nome", "idade", "cidade"]
valores = ["Alice", 30, "São Paulo"]
dicionario = dict(zip(chaves, valores))
print("Dicionário resultante:", dicionario)

#22. **Tuplas + Laços**: Crie uma tupla com coordenadas (x, y) e calcule a distância até a origem (0,0).
print("\n22. Tuplas + Laços: Crie uma tupla com coordenadas (x, y) e calcule a distância até a origem (0,0).\n")
coordenadas = (3, 4)
distancia = (coordenadas[0]**2 + coordenadas[1]**2)**0.5
print("Distância até a origem:", distancia)

#23. **Condicionais + Dicionários**: Crie um menu simples onde o usuário escolhe opções (ex: 1-ver estoque, 2-adicionar item).
print("\n23. Condicionais + Dicionários: Crie um menu simples onde o usuário escolhe opções (ex: 1-ver estoque, 2-adicionar item).\n")
estoque = {"maçã": 10, "banana": 5, "laranja": 8}
opcao = int(input("Escolha uma opção:\n1. Ver estoque\n2. Adicionar item\n"))
if opcao == 1:
    print("Estoque atual:")
    for fruta, quantidade in estoque.items():
        print(f"{fruta}: {quantidade}")
elif opcao == 2:
    fruta = input("Digite o nome da fruta: ")
    quantidade = int(input("Digite a quantidade: "))
    estoque[fruta] = estoque.get(fruta, 0) + quantidade
    print("Item adicionado com sucesso!")
else:
    print("Opção inválida.")

#24. **Laços + Strings**: Conte quantas vogais existem em uma string.
print("\n24. Laços + Strings: Conte quantas vogais existem em uma string.\n")
def contar_vogais(s):
    vogais = "aeiou"
    contador = 0
    for letra in s.lower():
        if letra in vogais:
            contador += 1
    return contador
frase = input("Digite uma frase: ")
print("Número de vogais:", contar_vogais(frase))

#25. **Funções + Dicionários**: Crie uma função que atualiza a idade de uma pessoa em um dicionário.
print("\n25. Funções + Dicionários: Crie uma função que atualiza a idade de uma pessoa em um dicionário.\n")
def atualizar_idade(dicionario, nome, nova_idade):
    if nome in dicionario:
        dicionario[nome] = nova_idade
        print(f"Idade de {nome} atualizada para {nova_idade}.")
    else:
        print(f"Pessoa {nome} não encontrada.")
pessoas = {"Alice": 30, "Bob": 25}
atualizar_idade(pessoas, "Alice", 31)
atualizar_idade(pessoas, "Charlie", 28)

#26. **Listas + Funções**: Crie uma função que filtra números pares de uma lista.
print("\n26. **Listas + Funções**: Crie uma função que filtra números pares de uma lista.\n")
def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]
numeros = [1, 2, 3, 4, 5, 6]
print("Números pares:", filtrar_pares(numeros))

#27. **Dicionários com Listas**: Crie um dicionário onde cada chave é um aluno e o valor é uma lista de notas.
print("\n27. **Dicionários com Listas**: Crie um dicionário onde cada chave é um aluno e o valor é uma lista de notas.\n")
alunos = {
    "Alice": [8, 9, 10],
    "Bob": [7, 6, 5],
    "Charlie": [10, 10, 10]
}
print("Dicionário de alunos e notas:", alunos)

#28. **Condicionais + Laços**: Verifique se todos os números em uma lista são positivos.
print("\n28. **Condicionais + Laços**: Verifique se todos os números em uma lista são positivos.\n")
def todos_positivos(lista):
    for num in lista:
        if num <= 0:
            return False
    return True
numeros = [1, 2, 3, 4, 5]
print("Todos os números são positivos?", todos_positivos(numeros))

#29. **Strings + Dicionários**: Conte a ocorrência de cada palavra em uma frase (ignore maiúsculas/minúsculas).
print("\n29. **Strings + Dicionários**: Conte a ocorrência de cada palavra em uma frase (ignore maiúsculas/minúsculas).\n")
def contar_palavras(frase):
    palavras = frase.lower().split()
    contador = {}
    for palavra in palavras:
        contador[palavra] = contador.get(palavra, 0) + 1
    return contador
frase = input("Digite uma frase: ")
print("Ocorrência de palavras:", contar_palavras(frase))

#30. **Tuplas + Condicionais**: Compare duas tuplas representando datas (ano, mês, dia) e veja qual é mais recente.
print("\n30. **Tuplas + Condicionais**: Compare duas tuplas representando datas (ano, mês, dia) e veja qual é mais recente.\n")
data1 = (2023, 10, 5)
data2 = (2022, 12, 25)
if data1 > data2:
    print("Data 1 é mais recente que Data 2.")
elif data1 < data2:
    print("Data 2 é mais recente que Data 1.")
else:
    print("As duas datas são iguais.")
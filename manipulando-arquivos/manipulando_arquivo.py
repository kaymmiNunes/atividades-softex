# Escrita de arquivos
arquivo = open('arquivo.txt', 'w')
arquivo.write('Olá mundo\n')
arquivo.write('Estou manipulando arquivos\n')
arquivo.close()

# Leitura de arquivos
arquivo = open('arquivo.txt', 'r')
print(arquivo.read())
arquivo.close()

# Leitura linha a linha
arquivo = open('arquivo.txt', 'r')
linha1 = arquivo.readline() # lê apenas uma linha do arquivo
linha2 = arquivo.readline()
print("Linha 1: ", linha1)
print("Linha 2: ", linha2)
arquivo.close()

# Leitura de todas as linhas
arquivo = open('arquivo.txt', 'r')
linhas = arquivo.readlines() # retorna uma lista com todas as linhas do arquivo
print(linhas)
arquivo.close()

# Acrescentar conteúdo ao arquivo
arquivo = open('arquivo.txt', 'a')
arquivo.write('Adicionando uma nova linha\n')
arquivo.close()

# Usando with para manipular arquivos
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo) # o arquivo é fechado automaticamente ao sair do bloco with

# Tratamento de exceções ao manipular arquivos
try:    
    with open('arquivo_inexistente.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo) # o arquivo é fechado automaticamente ao sair do bloco with
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as erro:
    print("Erro: {}".format(erro))
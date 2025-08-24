## Projetos Python - Lista de Exercícios

Este repositório contém diversos exercícios de Python desenvolvidos para estudo de conceitos 
básicos e intermediários, incluindo manipulação de strings, listas, dicionários, funções e validação de dados.

---

### Lista de Arquivos

### 1. `questao1.py` - Contar Vogais e Consoantes
- **Descrição:** Recebe uma frase do usuário, remove acentos e conta o número de vogais e consoantes.
- **Funcionalidades:**
  - Normaliza a frase para minúsculas.
  - Remove acentos.
  - Separa letras em vogais e consoantes.
  - Conta e exibe os resultados.

---

### 2. `questao2.py` - Verificar Palíndromo (com string invertida)
- **Descrição:** Recebe uma frase do usuário, remove acentos e espaços, e verifica se é um palíndromo.
- **Funcionalidades:**
  - Remove acentos e transforma em minúsculas.
  - Remove espaços.
  - Inverte a string e compara com a original.
  - Exibe se a frase é ou não palíndromo.

---

### 3. `questao2lista.py` - Verificar Palíndromo (com listas)
- **Descrição:** Verifica palíndromo usando listas de letras.
- **Funcionalidades:**
  - Cria listas separadas para as letras originais e invertidas.
  - Ignora caracteres que não sejam letras.
  - Compara as listas para determinar se a frase é palíndromo.
  - Mostra a frase normal e invertida.

---

### 4. `questao3dicionario.py` - Contagem de Frequência de Palavras
- **Descrição:** Recebe uma frase, remove acentos, separa em palavras e conta quantas vezes cada palavra aparece.
- **Funcionalidades:**
  - Normaliza a frase (minúsculo e sem acento).
  - Cria um dicionário para armazenar a frequência de cada palavra.
  - Percorre a lista de palavras e contabiliza.
  - Exibe cada palavra com a quantidade de ocorrências.

---

### 5. `questao4.py` - Validação de Senha
- **Descrição:** Verifica se a senha digitada pelo usuário é forte.
- **Regras de validação:**
  - Pelo menos 8 caracteres.
  - Contém pelo menos uma letra minúscula.
  - Contém pelo menos uma letra maiúscula.
  - Contém pelo menos um número.
- **Funcionalidades:**
  - Recebe a senha do usuário.
  - Verifica cada regra usando `len()` e `any()`.
  - Retorna mensagem de senha válida ou inválida.

---

### 6. `questao4descrito.py` - Validação de Senha (passo a passo)
- **Descrição:** Similar ao `questao4.py`, porém cada verificação é feita separadamente com mensagens específicas para cada regra.
- **Funcionalidades:**
  - Valida tamanho mínimo, letras minúsculas, maiúsculas e números.
  - Mostra mensagens detalhadas indicando quais regras foram atendidas ou não.

---

### 7. `questao5.py` - Gerar Acrônimo
- **Descrição:** Recebe uma frase e gera um acrônimo ignorando palavras comuns como preposições.
- **Funcionalidades:**
  - Remove palavras comuns definidas em uma lista (`de`, `da`, `do`, `das`, `dos`, `e`).
  - Separa as palavras restantes.
  - Pega a primeira letra de cada palavra e transforma em maiúscula.
  - Junta as letras com pontos para formar o acrônimo.
  - Exibe o acrônimo final.

---

## Observações Gerais

- Todos os códigos foram desenvolvidos com comentários detalhados explicando cada linha de comando.
- Objetivo principal: estudo de manipulação de strings, listas, dicionários e funções em Python.
- Técnicas utilizadas:
  - Uso de `unicodedata` para remover acentos.
  - Métodos de strings: `.lower()`, `.replace()`, `.split()`, `.join()`, `.isalpha()`.
  - Estruturas de dados: listas e dicionários.
  - Controle de fluxo: `for`, `if`, `else`.
  - Expressões geradoras e funções de agregação (`any()`, `len()`).

---

### Como Executar

Para executar qualquer um dos scripts Python deste repositório, siga os passos abaixo:

### Pré-requisitos
- Ter o Python instalado (versão 3.x recomendada).
- Ter um terminal ou prompt de comando disponível.

---

### Executando um script

1. Abra o terminal ou prompt de comando.
2. Navegue até a pasta onde o script está salvo, por exemplo:
   ```bash
   cd caminho/para/o/repositorio

---

### Autor

Kaymmi Nunes Barbosa
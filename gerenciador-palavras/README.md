## 🔍 Analisador de Palavras em Python

Este projeto é um **analisador de palavras em Python**, criado para identificar características de palavras digitadas pelo usuário. Ele permite estudar manipulação de strings, listas e condicionais na linguagem Python.

O programa lê uma frase digitada pelo usuário e avalia cada palavra, verificando se:

- Começa com a letra "A"  
- É um palíndromo  
- Possui 7 ou mais caracteres  
- É uma palavra comum (não se encaixa nas anteriores)

Palavras pequenas e comuns, como "de", "da", "do", "das", "dos" e "e", são automaticamente ignoradas na análise. Além disso, acentos são removidos para uma avaliação correta.

## 🚀 Funcionalidades

- Verifica se cada palavra começa com "A"  
- Identifica palíndromos  
- Detecta palavras longas (>=7 caracteres)  
- Ignora palavras pequenas ou comuns  
- Gera um resumo com a contagem de cada categoria  

## 🖥️ Exemplo de uso

```bash
Escreva várias palavras (separadas por espaço): 
"Árvore abacaxi radar e dos amêndoas anã"
Árvore: começa com A, é longa
abacaxi: começa com A, é longa
radar: é palíndromo
amêndoas: começa com A, é longa
anã: começa com A, é palíndromo

====RESUMO====

Palavras analisadas (não ignoradas): 5
Palavras que começam com A: 4
Palíndromos: 2
Palavras longas: 3
Palavras comuns: 1
```

## 🔧 Tecnologias utilizadas

- Python 3
- Biblioteca padrão unicodedata para manipulação de acentos

## 💡 Aprendizado

- Este projeto ajuda a praticar:
- Manipulação de strings e listas
- Uso de condicionais (if/else)
- Loops (for)
- Funções em Python (def)
- Tratamento de caracteres especiais e acentos

## 👤 Autor

Kaymmi Nunes Barbosa
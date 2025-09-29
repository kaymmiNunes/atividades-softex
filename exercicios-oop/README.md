## Exercícios de Python - Classes, Herança e Abstração

Este repositório contém **8 exercícios práticos** de Python, focados em **Programação Orientada a Objetos (POO)**, incluindo herança, polimorfismo, classes abstratas e propriedades.

## Conteúdo

### Exercício 1: Herança Simples de Atributos e Métodos
- Criação da classe base `Animal` com método `emitir_som()`.
- Criação da classe `Cachorro` que herda de `Animal` e sobrescreve `emitir_som()`.
- Demonstração de polimorfismo.

### Exercício 2: Classe Abstrata Básica
- Criação de uma classe abstrata `FormaGeometrica` com método abstrato `calcular_area()`.
- Criação da classe `Retangulo` que implementa `calcular_area()`.

### Exercício 3: Herança com Construtores
- Criação da classe base `Funcionario` com atributos `nome` e `salario`.
- Criação da classe `Gerente` que herda de `Funcionario`, adiciona `departamento` e usa `super()` para inicialização.

### Exercício 4: Abstração com Propriedades
- Criação da classe abstrata `Veiculo` com método abstrato `acelerar()` e propriedade abstrata `rodas`.
- Criação das classes `Carro` e `Moto` que implementam os métodos e propriedades.

### Exercício 5: Herança em Múltiplos Níveis (Hierarquia)
- Criação de hierarquia `DispositivoEletronico → Computador → Notebook`.
- Implementação de métodos específicos em cada nível e demonstração de chamada de métodos herdados.

### Exercício 6: Classe Abstrata com Método Concreto
- Criação da classe abstrata `ContaBancaria` com método abstrato `sacar()` e método concreto `verificar_saldo()`.
- Criação da classe `ContaCorrente` que implementa `sacar()` e manipula o saldo.

### Exercício 7: Múltiplas Classes Abstratas (Mixins Conceituais)
- Criação de classes abstratas `Percurso` e `Cobranca`.
- Criação da classe `Taxi` que herda de ambas e implementa `tempo_estimado()` e `calcular_tarifa()`.

### Exercício 8: Abstração e Herança para Sistema de Cadastro
- Criação da classe abstrata `Pessoa`.
- Criação das classes concretas `Cliente` e `Fornecedor`.
- Implementação de método `detalhes_de_cadastro()` e demonstração de polimorfismo com uma lista de objetos.


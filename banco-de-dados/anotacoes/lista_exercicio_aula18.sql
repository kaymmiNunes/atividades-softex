CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    cidade VARCHAR(100)
);

CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    valor DECIMAL(10,2),
    data_pedido DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

SELECT c.nome, p.valor, p.data_pedido
FROM clientes c
INNER JOIN pedidos p ON c.id_cliente = p.id_cliente;

SELECT c.nome, p.valor, p.data_pedido
FROM clientes c
LEFT JOIN pedidos p ON c.id_cliente = p.id_cliente;

SELECT c.nome, p.valor, p.data_pedido
FROM clientes c
RIGHT JOIN pedidos p ON c.id_cliente = p.id_cliente;

SELECT nome, cidade
FROM clientes
ORDER BY nome ASC;  -- ASC = crescente / DESC = decrescente

SELECT nome, cidade
FROM clientes
ORDER BY cidade DESC;

SELECT COUNT(*) AS total_pedidos FROM pedidos;
SELECT SUM(valor) AS total_vendas FROM pedidos;
SELECT AVG(valor) AS media_pedidos FROM pedidos;

SELECT c.nome, SUM(p.valor) AS total_gasto
FROM clientes c
INNER JOIN pedidos p ON c.id_cliente = p.id_cliente
GROUP BY c.nome;

SELECT c.cidade,
       COUNT(p.id_pedido) AS qtd_pedidos,
       SUM(p.valor) AS total_vendas
FROM clientes c
LEFT JOIN pedidos p ON c.id_cliente = p.id_cliente
GROUP BY c.cidade
ORDER BY total_vendas DESC;

from connection import Connection
from database import Database

class ClienteRepository:
    def __init__(self, database: Database):
        self.db = database

    def criar_cliente(self, nome, email, telefone):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cliente (nome, email, telefone) VALUES (?, ?, ?)",
                (nome, email, telefone)
            )
            conn.commit()
            return cursor.lastrowid

    def listar_clientes(self):
        with Connection() as (conn, cursor):
            cursor.execute("SELECT * FROM cliente ORDER BY id ASC")
            return cursor.fetchall()

    def buscar_cliente(self, cliente_id):
        with Connection() as (conn, cursor):
            cursor.execute("SELECT * FROM cliente WHERE id = ?", (cliente_id,))
            cursor.execute("SELECT * FROM cliente WHERE id = ?", (cliente_id,))
            return cursor.fetchone()

    def contar_clientes(self):
        with Connection() as (conn, cursor):
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM cliente")
            resultado = cursor.fetchone()
        return resultado[0] 

    def deletar_cliente(self, cliente_id):
        with Connection() as (conn, cursor):
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cliente WHERE id = ?", (cliente_id,))
            conn.commit()
            return cursor.rowcount
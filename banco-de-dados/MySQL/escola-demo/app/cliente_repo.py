from db import Database

class ClienteRepository:
    def __init__(self, db: Database):
        self.db = db

    def listar_todos(self):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente ORDER BY criado_em ASC"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        finally:
            conn.close()
    
    def adicionar_cliente(self, nome: str, email: str, telefone: str):
        sql = "INSERT INTO cliente (nome, email, telefone) VALUES (%s, %s, %s)"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (nome, email, telefone))
        conn.commit()
        novo_id = cursor.lastrowid 
        cursor.close()
        conn.close()
        return novo_id

    def buscar_por_id(self, cliente_id: int):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente WHERE id = %s"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql, (cliente_id,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        finally:
            conn.close()

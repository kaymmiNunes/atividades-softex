from database import Database
from cliente_repo import ClienteRepository

import os
import sqlite3

def ensure_schema(db_path: str):
    """Cria o banco/tabela caso não exista (útil para aula/exemplos)."""
    need_create = not os.path.exists(db_path)
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        if need_create:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                telefone TEXT,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
    finally:
        conn.close()

def main():
    db = Database()  # usa DB_PATH do .env ou escola_demo.db
    # cria esquema/dados iniciais se necessário (apenas para facilitar a aula)
    ensure_schema(db.path)

    repo = ClienteRepository(db)
    while True:
        print("\n============ Menu ============")
        print("1. Criar cliente")
        print("2. Buscar cliente por ID")
        print("3. Contar clientes")
        print("4. Deletar cliente por ID")
        print("5. Listar todos os clientes")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '6':
            print("\nSaindo...")
            break

        if escolha == '1':
            novo_id = repo.criar_cliente(
                nome = input("\nDigite o nome do cliente: "),
                email = input("\nDigite o email do cliente: "),
                telefone = input("\nDigite o telefone do cliente: ")
            )
            print(f"\nCliente criado com ID: {novo_id}")

        elif escolha == '2':
            cliente_id = int(input("\nDigite o ID do cliente: "))
            cliente = repo.buscar_cliente(cliente_id)
            if cliente is not None:
                print("\nCliente encontrado:", cliente)
            else:
                print("\nCliente não encontrado.")

        elif escolha == '3':
            total_clientes = repo.contar_clientes()
            print("\nTotal de clientes no banco de dados:", total_clientes)

        elif escolha == '4':
            try:
                cliente_id = int(input("\nDigite o ID do cliente a ser deletado: "))
            except ValueError:
                print("\nID inválido. Por favor, tente novamente.")
            
            confirma = input("\nDeletar o cliente selecionado? (s/n): ")
            if confirma.lower() == 's':
                linhas_deletadas = repo.deletar_cliente(cliente_id)
                print(f"\nNúmero de clientes deletados: {linhas_deletadas}")
            else:
                print("\nCliente não deletado.")
                
        elif escolha == '5':

            lista = repo.listar_clientes()
            print("\n=== Lista de Clientes ===")
            for c in lista:
                print(f"{c[0]}: {c[1]} — {c[2]} — {c[3]}")

if __name__ == "__main__":
    main()
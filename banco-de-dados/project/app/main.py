from db import Database
from cliente_repo import ClienteRepository

def main():
    db = Database()
    repo = ClienteRepository(db)

    clientes = repo.listar_todos()
    print("=== Clientes cadastrados ===")
    for c in clientes:
        print(f"{c['id']}: {c['nome']} — {c['email']} — {c['telefone']} — {c['criado_em']}")

    cliente = repo.buscar_por_id(4)
    print("=== Buscando cliente por ID ===")
    if cliente:
        print(f"{cliente['id']}: {cliente['nome']} — {cliente['email']} — {cliente['telefone']} — {cliente['criado_em']}")
    else:
        print("Cliente não encontrado.")

if __name__ == "__main__":
    main()
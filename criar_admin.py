import os
import mysql.connector
from dotenv import load_dotenv
from auth import gerar_hash_senha

load_dotenv()

def criar_primeiro_admin():
    nome = input("Digite o nome do administrador: ")
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")

    senha_criptografada = gerar_hash_senha(senha)

    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "epi_guard"),
        port=int(os.getenv("DB_PORT", 3306))
    )
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO administradores (nome, email, senha_hash) VALUES (%s, %s, %s)",
            (nome, email, senha_criptografada)
        )
        conexao.commit()
        print(f"\n✅ Administrador '{nome}' cadastrado com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro ao cadastrar: {e}")
    finally:
        cursor.close()
        conexao.close()

if __name__ == "__main__":
    criar_primeiro_admin()
"""
🗄️ Configuração do Banco de Dados

Aqui configuramos a conexão com o banco SQLite.
SQLite é um banco simples que salva tudo em um arquivo.
"""

from sqlmodel import SQLModel, Session, create_engine
import os

# Caminho para o arquivo do banco de dados
DATABASE_FILE = "database.db"
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

# Criando o engine (motor) do banco de dados
engine = create_engine(
    DATABASE_URL, 
    echo=False,  # Se True, mostra todas as queries SQL no console
    connect_args={"check_same_thread": False}  # Necessário para SQLite
)

def create_db_and_tables():
    """
    🏗️ Criar o banco e as tabelas
    
    Esta função é chamada quando a aplicação inicia.
    Cria todas as tabelas definidas nos modelos.
    """
    SQLModel.metadata.create_all(engine)
    print(f"✅ Banco de dados criado/conectado: {DATABASE_FILE}")

def get_session():
    """
    🔌 Obter uma sessão do banco
    
    Esta função é usada como dependência nas rotas.
    Cria uma sessão, usa e depois fecha automaticamente.
    """
    with Session(engine) as session:
        yield session

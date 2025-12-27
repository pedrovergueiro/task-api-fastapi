"""
📝 Task API - Aplicação Principal

Este é o arquivo principal da nossa API de tarefas.
Aqui configuramos o FastAPI e incluímos as rotas.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_db_and_tables
from routes import router

# Criando a aplicação FastAPI
app = FastAPI(
    title="📝 Task API",
    description="API simples para gerenciar suas tarefas diárias",
    version="1.0.0",
    docs_url="/docs",  # Documentação em /docs
    redoc_url="/redoc"  # Documentação alternativa em /redoc
)

# ========== CONFIGURAÇÃO CORS ==========
# Permite que o frontend acesse nossa API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem (para desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, PATCH, DELETE, etc.
    allow_headers=["*"],  # Permite JSON, Authorization, etc.
)
# =====================================

@app.on_event("startup")
def on_startup():
    """
    Função executada quando a aplicação inicia.
    Cria as tabelas do banco de dados se não existirem.
    """
    create_db_and_tables()

# Incluindo as rotas de tarefas
app.include_router(router)

@app.get("/")
def read_root():
    """
    Rota inicial da API.
    Retorna uma mensagem de boas-vindas.
    """
    return {
        "message": "🚀 Bem-vindo à Task API!",
        "docs": "/docs",
        "creator": "Pedro Vergueiro"
    }

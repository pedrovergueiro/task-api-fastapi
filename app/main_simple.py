"""
📝 Task API - Versão Simples

Versão simplificada da API para demonstração.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes_simple import router

# Criando a aplicação FastAPI
app = FastAPI(
    title="📝 Task API",
    description="API simples para gerenciar suas tarefas diárias",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo as rotas de tarefas
app.include_router(router)

@app.get("/")
def read_root():
    """
    Rota inicial da API.
    """
    return {
        "message": "🚀 Bem-vindo à Task API!",
        "docs": "/docs",
        "creator": "Pedro Vergueiro",
        "version": "Versão Simples - Funcional"
    }
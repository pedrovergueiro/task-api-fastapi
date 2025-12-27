"""
📊 Modelos de Dados Simples

Versão simplificada usando apenas Pydantic para demonstração.
"""

from pydantic import BaseModel
from typing import Optional, List

# Simulação de banco de dados em memória
tasks_db: List[dict] = []
next_id = 1

class Task(BaseModel):
    """
    Modelo da Tarefa
    
    Representa uma tarefa na aplicação.
    """
    id: Optional[int] = None
    title: str
    description: str
    done: bool = False

def get_next_id() -> int:
    """Gera o próximo ID disponível"""
    global next_id
    current_id = next_id
    next_id += 1
    return current_id
"""
📊 Modelos de Dados

Aqui definimos como os dados são estruturados no banco.
Usamos SQLModel que combina SQLAlchemy + Pydantic.
"""

from sqlmodel import SQLModel, Field

class Task(SQLModel, table=True):
    """
    Modelo da Tarefa
    
    Representa uma tarefa no banco de dados.
    Cada tarefa tem: id, título, descrição e status.
    """
    
    # ID único da tarefa (chave primária)
    id: int = Field(primary_key=True)
    
    # Título da tarefa (obrigatório)
    title: str
    
    # Descrição da tarefa (obrigatório)  
    description: str
    
    # Status da tarefa (False = pendente, True = concluída)
    done: bool = False
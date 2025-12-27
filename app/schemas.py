"""
📋 Schemas de Validação

Aqui definimos como os dados devem ser validados
quando chegam na API (entrada) e quando saem (resposta).
"""

from pydantic import BaseModel, Field
from typing import Optional

class TaskCreate(BaseModel):
    """
    Schema para criar uma nova tarefa.
    
    Usado quando alguém faz POST /tasks/
    """
    title: str = Field(
        min_length=1, 
        max_length=100,
        description="Título da tarefa"
    )
    description: str = Field(
        min_length=1, 
        max_length=500,
        description="Descrição detalhada da tarefa"
    )

class TaskUpdate(BaseModel):
    """
    Schema para atualizar uma tarefa existente.
    
    Usado quando alguém faz PATCH /tasks/{id}
    Todos os campos são opcionais.
    """
    title: Optional[str] = Field(
        None, 
        min_length=1, 
        max_length=100,
        description="Novo título da tarefa"
    )
    description: Optional[str] = Field(
        None, 
        min_length=1, 
        max_length=500,
        description="Nova descrição da tarefa"
    )
    done: Optional[bool] = Field(
        None,
        description="Status da tarefa (True = concluída, False = pendente)"
    )

class TaskResponse(BaseModel):
    """
    Schema para resposta da API.
    
    Define como a tarefa aparece quando é retornada.
    """
    id: int
    title: str
    description: str
    done: bool
    
    class Config:
        orm_mode = True

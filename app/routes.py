"""
🛣️ Rotas da API

Aqui definimos todos os endpoints (URLs) da nossa API.
Cada função representa uma operação que pode ser feita com tarefas.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from database import get_session
from sqlmodel import Session
from schemas import TaskCreate, TaskUpdate, TaskResponse
from crud import create_task, list_tasks, get_task_by_id, update_task, delete_task
from typing import List

# Criando o roteador para agrupar as rotas de tarefas
router = APIRouter(prefix="/tasks", tags=["📝 Tarefas"])

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def add_task(task: TaskCreate, session: Session = Depends(get_session)):
    """
    ➕ Criar uma nova tarefa
    
    Recebe os dados da tarefa e salva no banco de dados.
    """
    return create_task(session, task)

@router.get("/", response_model=List[TaskResponse])
def get_tasks(session: Session = Depends(get_session)):
    """
    📋 Listar todas as tarefas
    
    Retorna uma lista com todas as tarefas cadastradas.
    """
    return list_tasks(session)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, session: Session = Depends(get_session)):
    """
    🔍 Buscar uma tarefa específica
    
    Retorna os dados de uma tarefa pelo seu ID.
    """
    task = get_task_by_id(session, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return task

@router.patch("/{task_id}", response_model=TaskResponse)
def edit_task(task_id: int, task: TaskUpdate, session: Session = Depends(get_session)):
    """
    ✏️ Atualizar uma tarefa
    
    Permite modificar título, descrição ou status de uma tarefa.
    """
    updated_task = update_task(session, task_id, task)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return updated_task

@router.delete("/{task_id}")
def remove_task(task_id: int, session: Session = Depends(get_session)):
    """
    🗑️ Deletar uma tarefa
    
    Remove uma tarefa do banco de dados permanentemente.
    """
    success = delete_task(session, task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return {"message": "Tarefa deletada com sucesso!", "deleted": True}

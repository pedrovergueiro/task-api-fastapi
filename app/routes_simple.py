"""
🛣️ Rotas da API Simples

Versão simplificada das rotas.
"""

from fastapi import APIRouter, HTTPException, status
from schemas import TaskCreate, TaskUpdate, TaskResponse
from crud_simple import create_task, list_tasks, get_task_by_id, update_task, delete_task
from typing import List

# Criando o roteador para agrupar as rotas de tarefas
router = APIRouter(prefix="/tasks", tags=["📝 Tarefas"])

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def add_task(task: TaskCreate):
    """
    ➕ Criar uma nova tarefa
    """
    return create_task(task)

@router.get("/", response_model=List[TaskResponse])
def get_tasks():
    """
    📋 Listar todas as tarefas
    """
    return list_tasks()

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    """
    🔍 Buscar uma tarefa específica
    """
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return task

@router.patch("/{task_id}", response_model=TaskResponse)
def edit_task(task_id: int, task: TaskUpdate):
    """
    ✏️ Atualizar uma tarefa
    """
    updated_task = update_task(task_id, task)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return updated_task

@router.delete("/{task_id}")
def remove_task(task_id: int):
    """
    🗑️ Deletar uma tarefa
    """
    success = delete_task(task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return {"message": "Tarefa deletada com sucesso!", "deleted": True}
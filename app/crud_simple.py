"""
🔧 Operações CRUD Simples

Versão simplificada usando lista em memória.
"""

from models_simple import Task, tasks_db, get_next_id
from schemas import TaskCreate, TaskUpdate
from typing import List, Optional

def create_task(task_data: TaskCreate) -> Task:
    """
    ➕ Criar uma nova tarefa
    """
    task_dict = task_data.dict()
    task_dict["id"] = get_next_id()
    task_dict["done"] = False
    
    tasks_db.append(task_dict)
    return Task(**task_dict)

def list_tasks() -> List[Task]:
    """
    📋 Listar todas as tarefas
    """
    return [Task(**task) for task in tasks_db]

def get_task_by_id(task_id: int) -> Optional[Task]:
    """
    🔍 Buscar uma tarefa pelo ID
    """
    for task in tasks_db:
        if task["id"] == task_id:
            return Task(**task)
    return None

def update_task(task_id: int, task_data: TaskUpdate) -> Optional[Task]:
    """
    ✏️ Atualizar uma tarefa existente
    """
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            update_data = task_data.dict(exclude_unset=True)
            tasks_db[i].update(update_data)
            return Task(**tasks_db[i])
    return None

def delete_task(task_id: int) -> bool:
    """
    🗑️ Deletar uma tarefa
    """
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            del tasks_db[i]
            return True
    return False
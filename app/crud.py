"""
🔧 Operações CRUD

CRUD = Create, Read, Update, Delete
Aqui ficam todas as operações que fazemos no banco de dados.
"""

from sqlmodel import select, Session
from models import Task
from schemas import TaskCreate, TaskUpdate
from typing import List, Optional

def create_task(session: Session, task_data: TaskCreate) -> Task:
    """
    ➕ Criar uma nova tarefa no banco
    
    Recebe os dados da tarefa, cria um objeto Task e salva no banco.
    """
    # Converter os dados do schema para o modelo
    task = Task(**task_data.dict())
    
    # Adicionar à sessão e salvar
    session.add(task)
    session.commit()
    session.refresh(task)  # Atualiza o objeto com dados do banco (como ID)
    
    return task

def list_tasks(session: Session) -> List[Task]:
    """
    📋 Listar todas as tarefas
    
    Busca todas as tarefas no banco e retorna uma lista.
    """
    statement = select(Task)
    tasks = session.exec(statement).all()
    return tasks

def get_task_by_id(session: Session, task_id: int) -> Optional[Task]:
    """
    🔍 Buscar uma tarefa pelo ID
    
    Retorna a tarefa se encontrar, ou None se não existir.
    """
    return session.get(Task, task_id)

def update_task(session: Session, task_id: int, task_data: TaskUpdate) -> Optional[Task]:
    """
    ✏️ Atualizar uma tarefa existente
    
    Busca a tarefa pelo ID e atualiza apenas os campos fornecidos.
    """
    # Buscar a tarefa
    task = session.get(Task, task_id)
    if not task:
        return None

    # Pegar apenas os campos que foram fornecidos (não None)
    update_data = task_data.dict(exclude_unset=True)
    
    # Atualizar cada campo
    for field, value in update_data.items():
        setattr(task, field, value)

    # Salvar as mudanças
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task

def delete_task(session: Session, task_id: int) -> bool:
    """
    🗑️ Deletar uma tarefa
    
    Busca a tarefa pelo ID e remove do banco.
    Retorna True se deletou, False se não encontrou.
    """
    task = session.get(Task, task_id)
    if not task:
        return False

    session.delete(task)
    session.commit()
    return True

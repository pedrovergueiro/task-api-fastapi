from fastapi import APIRouter, Depends, HTTPException
from app.database import get_session
from sqlmodel import Session
from app.schemas import TaskCreate, TaskUpdate
from app.crud import create_task, list_tasks, update_task, delete_task

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def add_task(task: TaskCreate, session: Session = Depends(get_session)):
    return create_task(session, task)

@router.get("/")
def get_tasks(session: Session = Depends(get_session)):
    return list_tasks(session)

@router.patch("/{task_id}")
def edit_task(task_id: int, task: TaskUpdate, session: Session = Depends(get_session)):
    updated = update_task(session, task_id, task)
    if not updated:
        raise HTTPException(404, "Task not found")
    return updated

@router.delete("/{task_id}")
def remove_task(task_id: int, session: Session = Depends(get_session)):
    ok = delete_task(session, task_id)
    if not ok:
        raise HTTPException(404, "Task not found")
    return {"deleted": True}

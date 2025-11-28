from sqlmodel import select, Session
from app.models import Task

def create_task(session: Session, data):
    task = Task(**data.dict())
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def list_tasks(session: Session):
    return session.exec(select(Task)).all()

def update_task(session: Session, task_id: int, data):
    task = session.get(Task, task_id)
    if not task:
        return None

    updates = data.dict(exclude_unset=True)
    for key, value in updates.items():
        setattr(task, key, value)

    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def delete_task(session: Session, task_id: int):
    task = session.get(Task, task_id)
    if not task:
        return False

    session.delete(task)
    session.commit()
    return True

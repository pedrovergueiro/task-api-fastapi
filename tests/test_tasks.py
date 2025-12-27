"""
🧪 Testes da API de Tarefas

Aqui testamos se nossa API está funcionando corretamente.
Usamos pytest para rodar os testes automaticamente.
"""

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from app.main import app
from app.database import get_session

# Configuração do banco de teste (em memória)
@pytest.fixture(name="session")
def session_fixture():
    """
    Cria um banco de dados temporário para os testes.
    Cada teste usa um banco limpo.
    """
    engine = create_engine(
        "sqlite://", 
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    """
    Cria um cliente de teste que usa o banco temporário.
    """
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

def test_read_root(client: TestClient):
    """
    🏠 Testa se a página inicial funciona
    """
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Pedro Vergueiro" in data["creator"]

def test_create_task(client: TestClient):
    """
    ➕ Testa se conseguimos criar uma tarefa
    """
    task_data = {
        "title": "Estudar FastAPI",
        "description": "Ler documentação e fazer exercícios"
    }
    
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["description"] == task_data["description"]
    assert data["done"] == False
    assert "id" in data

def test_list_tasks_empty(client: TestClient):
    """
    📋 Testa se a lista de tarefas vazia funciona
    """
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []

def test_list_tasks_with_data(client: TestClient):
    """
    📋 Testa se conseguimos listar tarefas
    """
    # Criar uma tarefa primeiro
    task_data = {
        "title": "Tarefa de Teste",
        "description": "Descrição de teste"
    }
    client.post("/tasks/", json=task_data)
    
    # Listar tarefas
    response = client.get("/tasks/")
    assert response.status_code == 200
    
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == task_data["title"]

def test_get_task_by_id(client: TestClient):
    """
    🔍 Testa se conseguimos buscar uma tarefa pelo ID
    """
    # Criar uma tarefa
    task_data = {
        "title": "Tarefa Específica",
        "description": "Para testar busca por ID"
    }
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Buscar a tarefa
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == task_data["title"]

def test_get_task_not_found(client: TestClient):
    """
    🔍 Testa se retorna erro quando tarefa não existe
    """
    response = client.get("/tasks/999")
    assert response.status_code == 404

def test_update_task(client: TestClient):
    """
    ✏️ Testa se conseguimos atualizar uma tarefa
    """
    # Criar uma tarefa
    task_data = {
        "title": "Tarefa Original",
        "description": "Descrição original"
    }
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Atualizar a tarefa
    update_data = {
        "title": "Tarefa Atualizada",
        "done": True
    }
    response = client.patch(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["title"] == update_data["title"]
    assert data["done"] == True
    assert data["description"] == task_data["description"]  # Não mudou

def test_update_task_not_found(client: TestClient):
    """
    ✏️ Testa se retorna erro ao tentar atualizar tarefa inexistente
    """
    update_data = {"title": "Não vai funcionar"}
    response = client.patch("/tasks/999", json=update_data)
    assert response.status_code == 404

def test_delete_task(client: TestClient):
    """
    🗑️ Testa se conseguimos deletar uma tarefa
    """
    # Criar uma tarefa
    task_data = {
        "title": "Tarefa para Deletar",
        "description": "Será removida"
    }
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Deletar a tarefa
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["deleted"] == True
    
    # Verificar se foi deletada
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404

def test_delete_task_not_found(client: TestClient):
    """
    🗑️ Testa se retorna erro ao tentar deletar tarefa inexistente
    """
    response = client.delete("/tasks/999")
    assert response.status_code == 404

def test_create_task_validation(client: TestClient):
    """
    ✅ Testa se a validação de dados funciona
    """
    # Tentar criar tarefa sem título
    invalid_data = {
        "description": "Sem título"
    }
    response = client.post("/tasks/", json=invalid_data)
    assert response.status_code == 422  # Erro de validação
    
    # Tentar criar tarefa com título vazio
    invalid_data = {
        "title": "",
        "description": "Título vazio"
    }
    response = client.post("/tasks/", json=invalid_data)
    assert response.status_code == 422  # Erro de validação

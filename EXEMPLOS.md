# 📚 Exemplos de Uso da Task API

Este arquivo contém exemplos práticos de como usar nossa API de tarefas.

## 🚀 Iniciando a API

```bash
# Método 1: Usando o script run.py
python run.py

# Método 2: Usando uvicorn diretamente
cd app
uvicorn main:app --reload
```

## 🌐 Testando no Navegador

Após iniciar a API, abra no navegador:
- **Documentação interativa**: http://localhost:8000/docs
- **Página inicial**: http://localhost:8000/

## 📝 Exemplos com cURL

### 1. Criar uma tarefa
```bash
curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar FastAPI",
    "description": "Ler documentação e fazer exercícios práticos"
  }'
```

### 2. Listar todas as tarefas
```bash
curl -X GET "http://localhost:8000/tasks/"
```

### 3. Buscar uma tarefa específica
```bash
curl -X GET "http://localhost:8000/tasks/1"
```

### 4. Marcar tarefa como concluída
```bash
curl -X PATCH "http://localhost:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```

### 5. Atualizar título e descrição
```bash
curl -X PATCH "http://localhost:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar FastAPI - Concluído",
    "description": "Documentação lida e exercícios feitos!"
  }'
```

### 6. Deletar uma tarefa
```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

## 🐍 Exemplos com Python

### Usando requests
```python
import requests

# URL base da API
BASE_URL = "http://localhost:8000"

# 1. Criar uma tarefa
def criar_tarefa():
    data = {
        "title": "Aprender Python",
        "description": "Estudar conceitos básicos e avançados"
    }
    response = requests.post(f"{BASE_URL}/tasks/", json=data)
    print("Tarefa criada:", response.json())
    return response.json()["id"]

# 2. Listar tarefas
def listar_tarefas():
    response = requests.get(f"{BASE_URL}/tasks/")
    print("Todas as tarefas:", response.json())

# 3. Marcar como concluída
def concluir_tarefa(task_id):
    data = {"done": True}
    response = requests.patch(f"{BASE_URL}/tasks/{task_id}", json=data)
    print("Tarefa atualizada:", response.json())

# 4. Deletar tarefa
def deletar_tarefa(task_id):
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    print("Resultado:", response.json())

# Exemplo de uso
if __name__ == "__main__":
    # Criar uma tarefa
    task_id = criar_tarefa()
    
    # Listar todas
    listar_tarefas()
    
    # Marcar como concluída
    concluir_tarefa(task_id)
    
    # Deletar
    deletar_tarefa(task_id)
```

### Usando httpx (async)
```python
import asyncio
import httpx

async def exemplo_async():
    async with httpx.AsyncClient() as client:
        # Criar tarefa
        response = await client.post("http://localhost:8000/tasks/", json={
            "title": "Tarefa Async",
            "description": "Criada com httpx"
        })
        print("Tarefa criada:", response.json())
        
        # Listar tarefas
        response = await client.get("http://localhost:8000/tasks/")
        print("Tarefas:", response.json())

# Executar
asyncio.run(exemplo_async())
```

## 🧪 Rodando os Testes

```bash
# Instalar dependências de teste (se ainda não instalou)
pip install pytest pytest-asyncio httpx

# Rodar todos os testes
pytest

# Rodar com mais detalhes
pytest -v

# Rodar um teste específico
pytest tests/test_tasks.py::test_create_task -v
```

## 📊 Estrutura das Respostas

### Tarefa (Task)
```json
{
  "id": 1,
  "title": "Estudar FastAPI",
  "description": "Ler documentação oficial",
  "done": false,
  "created_at": "2024-01-15T10:30:00.123456"
}
```

### Lista de Tarefas
```json
[
  {
    "id": 1,
    "title": "Primeira tarefa",
    "description": "Descrição da primeira",
    "done": true,
    "created_at": "2024-01-15T10:30:00.123456"
  },
  {
    "id": 2,
    "title": "Segunda tarefa", 
    "description": "Descrição da segunda",
    "done": false,
    "created_at": "2024-01-15T11:00:00.123456"
  }
]
```

## ❌ Tratamento de Erros

### Tarefa não encontrada (404)
```json
{
  "detail": "Tarefa com ID 999 não encontrada"
}
```

### Dados inválidos (422)
```json
{
  "detail": [
    {
      "loc": ["body", "title"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

## 🎯 Dicas Úteis

1. **Use a documentação interativa**: Acesse `/docs` para testar a API no navegador
2. **Valide os dados**: A API valida automaticamente título e descrição
3. **IDs são únicos**: Cada tarefa tem um ID único gerado automaticamente
4. **Timestamps**: A data de criação é salva automaticamente
5. **Testes**: Sempre rode os testes antes de fazer mudanças no código
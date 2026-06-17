# Task API — FastAPI

Uma API REST completa pra gerenciamento de tarefas. Foi o projeto onde me aprofundei de verdade no ecossistema FastAPI e aprendi como construir um backend mais robusto.

Implementei autenticação com JWT, banco de dados com SQLAlchemy, validação de dados com Pydantic e uma cobertura básica de testes. Provavelmente o projeto de backend mais completo que fiz até então.

## O que aprendi
- Como o FastAPI gera documentação automática (Swagger/ReDoc)
- Autenticação JWT e como proteger rotas
- SQLAlchemy para modelagem e consulta de dados
- A importância de escrever testes desde o início

## Como rodar

```bash
pip install -r requirements.txt
python run.py
# Acesse: http://localhost:8000/docs
```

## Endpoints principais
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | /auth/register | Criar conta |
| POST | /auth/login | Autenticar |
| GET | /tasks | Listar tarefas |
| POST | /tasks | Criar tarefa |
| PUT | /tasks/{id} | Atualizar |
| DELETE | /tasks/{id} | Remover |

## Stack
Python · FastAPI · SQLAlchemy · PostgreSQL · JWT · pytest

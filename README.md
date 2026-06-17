# Task API — FastAPI

API REST pra gerenciamento de tarefas que construí pra aprender como funciona um backend completo de verdade — não o tutorial de 20 minutos do YouTube, mas um projeto com autenticação, banco de dados, testes e documentação.

Implementei autenticação JWT do zero (sem biblioteca mágica), modelei o banco com SQLAlchemy, escrevi testes com pytest e configurei o Swagger automático que o FastAPI gera. A parte de JWT foi onde mais aprendi — entender como o token é assinado, validado e invalidado fez muita coisa fazer sentido.

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/auth/register` | Criar conta |
| POST | `/auth/login` | Autenticar e receber token |
| GET | `/tasks` | Listar tarefas do usuário autenticado |
| POST | `/tasks` | Criar tarefa |
| PUT | `/tasks/{id}` | Atualizar tarefa |
| DELETE | `/tasks/{id}` | Remover tarefa |

## Como rodar

```bash
pip install -r requirements.txt
python run.py
# Documentação: http://localhost:8000/docs
```

## Stack
Python · FastAPI · SQLAlchemy · PostgreSQL · JWT · pytest

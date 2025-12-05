# Task API - FastAPI REST API

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

**API REST completa com FastAPI - CRUD | Autenticação JWT | PostgreSQL | Testes Automatizados**

[![Code Quality](https://img.shields.io/badge/Code-Quality-green?style=flat-square)](https://github.com/pedrovergueiro/task-api-fastapi)
[![Tests](https://img.shields.io/badge/Tests-Passing-green?style=flat-square)](https://github.com/pedrovergueiro/task-api-fastapi)

</div>

---

## 📋 Sobre o Projeto

API REST production-ready desenvolvida com **FastAPI** implementando um sistema completo de gerenciamento de tarefas. O projeto demonstra boas práticas de desenvolvimento backend incluindo autenticação JWT, validação de dados, testes automatizados e documentação automática.

### 🎯 Objetivo

Criar uma API REST escalável e bem arquitetada que sirva como referência para desenvolvimento backend profissional, demonstrando:
- Design de APIs RESTful
- Autenticação e autorização
- Validação de dados robusta
- Testes automatizados
- Documentação automática

---

## 🚀 Tecnologias

### Core
- **Python 3.8+** - Linguagem principal
- **FastAPI** - Framework web moderno e rápido
- **PostgreSQL** - Banco de dados relacional
- **SQLAlchemy** - ORM para Python
- **Pydantic** - Validação de dados

### Testes & Qualidade
- **Pytest** - Framework de testes
- **Pytest-cov** - Cobertura de testes
- **Black** - Formatação de código
- **Flake8** - Linting

### Autenticação
- **JWT** - JSON Web Tokens
- **Passlib** - Hash de senhas
- **Python-jose** - Manipulação de JWT

---

## 📊 Features Principais

### 🔐 Autenticação & Autorização
- ✅ Sistema de autenticação JWT completo
- ✅ Hash seguro de senhas com bcrypt
- ✅ Middleware de autenticação
- ✅ Proteção de rotas sensíveis

### 📝 CRUD Completo
- ✅ Criar, ler, atualizar e deletar tarefas
- ✅ Validação de dados com Pydantic
- ✅ Tratamento de erros robusto
- ✅ Paginação de resultados

### 🧪 Testes
- ✅ Testes unitários completos
- ✅ Testes de integração
- ✅ Cobertura de código > 80%
- ✅ CI/CD com GitHub Actions

### 📚 Documentação
- ✅ Documentação automática com Swagger/OpenAPI
- ✅ Endpoints documentados
- ✅ Exemplos de requisições/respostas
- ✅ Schema de dados completo

---

## 💻 Instalação

### Pré-requisitos

```bash
Python 3.8 ou superior
PostgreSQL 12+
pip (gerenciador de pacotes Python)
```

### Instalação

```bash
# Clone o repositório
git clone https://github.com/pedrovergueiro/task-api-fastapi.git
cd task-api-fastapi

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas configurações

# Execute as migrations
alembic upgrade head

# Execute os testes
pytest

# Inicie o servidor
uvicorn main:app --reload
```

---

## 🏗️ Arquitetura

```
task-api-fastapi/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── auth.py      # Rotas de autenticação
│   │   │   └── tasks.py     # Rotas de tarefas
│   │   └── dependencies.py  # Dependências FastAPI
│   ├── core/
│   │   ├── config.py        # Configurações
│   │   ├── security.py      # Segurança e JWT
│   │   └── database.py      # Conexão com banco
│   ├── models/
│   │   ├── task.py          # Modelo de tarefa
│   │   └── user.py          # Modelo de usuário
│   ├── schemas/
│   │   ├── task.py          # Schemas Pydantic
│   │   └── user.py          # Schemas de usuário
│   └── main.py              # Aplicação principal
├── tests/                   # Testes automatizados
├── alembic/                 # Migrations
├── requirements.txt
└── README.md
```

### 🎨 Princípios de Design

- **Separação de Responsabilidades**: Cada módulo tem função específica
- **Dependency Injection**: Uso de dependências do FastAPI
- **Type Hints**: Tipagem completa do código
- **SOLID**: Princípios de design orientado a objetos
- **Clean Architecture**: Camadas bem definidas

---

## 📡 Endpoints Principais

### Autenticação
- `POST /api/auth/register` - Registrar novo usuário
- `POST /api/auth/login` - Login e obter token JWT
- `GET /api/auth/me` - Obter usuário atual

### Tarefas
- `GET /api/tasks` - Listar tarefas (com paginação)
- `GET /api/tasks/{id}` - Obter tarefa específica
- `POST /api/tasks` - Criar nova tarefa
- `PUT /api/tasks/{id}` - Atualizar tarefa
- `DELETE /api/tasks/{id}` - Deletar tarefa

---

## 🧪 Executando Testes

```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=app --cov-report=html

# Executar testes específicos
pytest tests/test_tasks.py
```

---

## 📚 Documentação da API

Após iniciar o servidor, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

---

## 🎯 Casos de Uso

### Exemplo: Criar Tarefa

```python
import requests

# Autenticar
response = requests.post("http://localhost:8000/api/auth/login", json={
    "username": "usuario",
    "password": "senha"
})
token = response.json()["access_token"]

# Criar tarefa
headers = {"Authorization": f"Bearer {token}"}
response = requests.post("http://localhost:8000/api/tasks", json={
    "title": "Nova tarefa",
    "description": "Descrição da tarefa",
    "completed": False
}, headers=headers)
```

---

## 📈 Performance

- ✅ Resposta média < 50ms
- ✅ Suporte a múltiplas requisições simultâneas
- ✅ Conexão pool com banco de dados
- ✅ Cache de queries frequentes

---

## 🔒 Segurança

- ✅ Senhas hasheadas com bcrypt
- ✅ Tokens JWT com expiração
- ✅ Validação de entrada de dados
- ✅ Proteção contra SQL Injection (ORM)
- ✅ CORS configurado

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Desenvolvedor

**Pedro L. Vergueiro**

- 📧 Email: pedrolv.fsilva@gmail.com
- 💼 LinkedIn: [Pedro L. Vergueiro](https://www.linkedin.com/in/pedro-vergueiro)
- 🌐 GitHub: [@pedrovergueiro](https://github.com/pedrovergueiro)

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

Made with ❤️ by Pedro L. Vergueiro

</div>

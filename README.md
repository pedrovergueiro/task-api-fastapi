👋 Olá! Eu sou o Pedro Vergueiro

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-316192?style=for-the-badge&logo=sqlite&logoColor=white)

**📝 Minha jornada aprendendo FastAPI - API de Tarefas**

</div>

## 🎯 Por que criei este projeto?

Este projeto foi desenvolvido por mim para **fixar e praticar** os conceitos de **FastAPI** que estou estudando. Como estudante de Engenharia de Software, acredito que a melhor forma de aprender é colocando a mão na massa!

Decidi criar uma API simples de gerenciamento de tarefas porque:
- É um problema real que todos enfrentamos
- Permite praticar operações CRUD básicas
- É fácil de entender e expandir
- Serve como base para projetos maiores

## 🧠 O que aprendi construindo isso

Durante o desenvolvimento desta API, consegui fixar vários conceitos importantes:

### 📚 **Conceitos de FastAPI que pratiquei:**
- **Rotas e Endpoints**: Como criar URLs que respondem a diferentes métodos HTTP
- **Validação de Dados**: Usando Pydantic para garantir que os dados estão corretos
- **Documentação Automática**: FastAPI gera docs lindas automaticamente!
- **Tratamento de Erros**: Como retornar erros HTTP apropriados
- **Middleware CORS**: Para permitir acesso de frontends

### 🔧 **Habilidades técnicas desenvolvidas:**
- Estruturação de projetos Python
- Separação de responsabilidades (models, routes, crud)
- Testes automatizados com pytest
- Documentação de código
- Versionamento com Git

```python
class MeuAprendizado:
    def __init__(self):
        self.nome = "Pedro Vergueiro"
        self.projeto = "Task API com FastAPI"
        self.objetivo = "Fixar conceitos de desenvolvimento de APIs"
        
    def o_que_implementei(self):
        return {
            "endpoints": ["GET", "POST", "PATCH", "DELETE"],
            "validacao": "Pydantic schemas",
            "documentacao": "Swagger UI automática",
            "testes": "pytest com cobertura completa",
            "estrutura": "Separação clara de responsabilidades"
        }
    
    def proximos_passos(self):
        return [
            "Adicionar autenticação JWT",
            "Implementar banco de dados real",
            "Deploy na nuvem",
            "Criar frontend"
        ]

meu_projeto = MeuAprendizado()
print("Cada linha de código foi uma lição aprendida! 🚀")
```

## 🛠️ Tecnologias que usei e por quê

Escolhi cada tecnologia pensando no aprendizado e na simplicidade:

**🐍 Python + FastAPI**
- FastAPI é moderno, rápido e tem documentação excelente
- Perfeito para quem está começando com APIs
- Validação automática de dados
- Documentação interativa gerada automaticamente

**💾 Duas versões de persistência**
- **Versão Simples**: Lista em memória (para focar no FastAPI)
- **Versão Avançada**: SQLite + SQLModel (para aprender banco de dados)

**🧪 Testes com pytest**
- Aprendi a importância de testar cada endpoint
- Cobertura completa das funcionalidades
- Testes automatizados que rodam a cada mudança

## 📖 Como estruturei o projeto

Organizei tudo pensando em **clareza** e **facilidade de entendimento**:

```
task-api-fastapi/
├── app/                          # 📁 Código principal da API
│   ├── main_simple.py           # 🚀 Versão funcionando (recomendada)
│   ├── models_simple.py         # 📊 Como os dados são organizados
│   ├── routes_simple.py         # 🛣️ Endpoints da API
│   ├── crud_simple.py           # 🔧 Operações no "banco"
│   ├── schemas.py               # ✅ Validação de dados
│   └── database.py              # 💾 Configuração do banco (versão avançada)
├── tests/                       # 🧪 Testes automatizados
├── EXEMPLOS.md                  # 📚 Como usar a API na prática
├── COMO_USAR.md                 # 🎯 Guia rápido de uso
└── README.md                    # 📖 Este arquivo
```

### 🤔 Por que separei assim?

- **models**: Define como os dados são estruturados
- **routes**: Define quais URLs existem e o que fazem
- **crud**: Operações básicas (Create, Read, Update, Delete)
- **schemas**: Valida se os dados estão no formato correto
- **tests**: Garante que tudo funciona como esperado

## 🏃‍♂️ Como rodar meu projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/pedrovergueiro/task-api-fastapi.git
cd task-api-fastapi
```

### 2️⃣ Criar ambiente virtual (aprendi que é boa prática!)
```bash
# Criar o ambiente isolado
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux/Mac  
source venv/bin/activate
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar a API
```bash
# Entrar na pasta do código
cd app

# Iniciar o servidor (uso a versão simples que funciona 100%)
uvicorn main_simple:app --reload
```

### 5️⃣ Testar se deu certo
Abra o navegador em: **http://localhost:8000/docs**

🎉 **Pronto!** Você verá a documentação interativa que o FastAPI criou automaticamente!

## 📝 Duas versões para diferentes níveis de aprendizado

### ✅ **Versão Simples** (Recomendada para começar)
- **Arquivo**: `main_simple.py`
- **Banco**: Lista em memória
- **Vantagem**: Foco total no FastAPI, sem complicações
- **Desvantagem**: Dados se perdem ao reiniciar

### 🚧 **Versão com Banco** (Para quando dominar o básico)
- **Arquivo**: `main.py`
- **Banco**: SQLite com SQLModel
- **Vantagem**: Dados persistem, mais realista
- **Status**: Ainda ajustando compatibilidades

**💡 Dica**: Comece com a versão simples para entender FastAPI, depois evolua para a versão com banco!

## 📁 Como o Projeto está Organizado

```
task-api-fastapi/
├── app/                    # Código principal
│   ├── main.py            # Arquivo principal da API
│   ├── models.py          # Como os dados são salvos
│   ├── schemas.py         # Validação dos dados
│   ├── routes.py          # Rotas da API (/tasks)
│   ├── crud.py            # Operações no banco
│   └── database.py        # Conexão com banco
├── tests/                 # Testes da aplicação
├── database.db           # Banco SQLite (criado automaticamente)
├── requirements.txt       # Dependências do projeto
└── README.md             # Este arquivo
```

## 🎯 O que minha API faz (e como implementei)

Criei uma API REST completa para gerenciar tarefas. Aqui está o que cada endpoint faz:

### ➕ **Criar Tarefa** - `POST /tasks/`
```python
# O que aprendi: Como receber dados JSON e validar
@router.post("/", response_model=TaskResponse)
def add_task(task: TaskCreate):
    # Pydantic valida automaticamente os dados!
    return create_task(task)
```

**Exemplo de uso:**
```bash
curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar FastAPI",
    "description": "Ler docs e fazer exercícios"
  }'
```

### 📋 **Listar Tarefas** - `GET /tasks/`
```python
# O que aprendi: Como retornar listas de dados
@router.get("/", response_model=List[TaskResponse])
def get_tasks():
    return list_tasks()
```

### 🔍 **Buscar Tarefa** - `GET /tasks/{id}`
```python
# O que aprendi: Parâmetros de URL e tratamento de erros
@router.get("/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)
    if not task:
        # Aprendi a retornar erros HTTP apropriados
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task
```

### ✏️ **Atualizar Tarefa** - `PATCH /tasks/{id}`
```python
# O que aprendi: Atualizações parciais de dados
@router.patch("/{task_id}")
def edit_task(task_id: int, task: TaskUpdate):
    # TaskUpdate permite campos opcionais
    return update_task(task_id, task)
```

### 🗑️ **Deletar Tarefa** - `DELETE /tasks/{id}`
```python
# O que aprendi: Operações de remoção
@router.delete("/{task_id}")
def remove_task(task_id: int):
    success = delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404)
    return {"message": "Tarefa deletada!", "deleted": True}
```

## 🧪 Como implementei os testes

Aprendi que testar é fundamental! Criei testes para cada funcionalidade:

```python
def test_create_task(client):
    """Testa se consigo criar uma tarefa"""
    task_data = {
        "title": "Estudar FastAPI",
        "description": "Ler documentação"
    }
    
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201  # Created
    
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["done"] == False  # Nova tarefa sempre pendente
```

**Para rodar os testes:**
```bash
# Rodar todos os testes
pytest

# Ver detalhes
pytest -v

# Ver cobertura
pytest --cov=app
```

### 🎓 O que aprendi sobre testes:
- **Fixtures**: Como criar dados de teste reutilizáveis
- **Mocking**: Como simular banco de dados para testes
- **Assertions**: Como verificar se o resultado está correto
- **Cobertura**: Garantir que testei todas as funcionalidades

## 💡 Desafios que enfrentei e como resolvi

### 🔧 **Problema 1: Compatibilidade de versões**
**Desafio**: SQLModel com Pydantic v2 deu conflito
**Solução**: Criei duas versões - uma simples que funciona, outra para evoluir

### 📚 **Problema 2: Estrutura do projeto**
**Desafio**: Como organizar o código de forma clara?
**Solução**: Separei responsabilidades em arquivos diferentes

### 🧪 **Problema 3: Testes com banco de dados**
**Desafio**: Como testar sem afetar dados reais?
**Solução**: Aprendi a usar banco em memória para testes

### 📖 **Problema 4: Documentação**
**Desafio**: Como deixar o código fácil de entender?
**Solução**: Comentários em português e README detalhado

## 📚 Principais conceitos que fixei

### 🎯 **FastAPI Fundamentals**
- **Decoradores de rota**: `@app.get()`, `@app.post()`, etc.
- **Dependency Injection**: Como usar `Depends()` para injetar dependências
- **Response Models**: Definir formato de resposta com Pydantic
- **Status Codes**: Retornar códigos HTTP apropriados (200, 201, 404, etc.)

### 🔍 **Validação de Dados**
- **Pydantic Models**: Validação automática de entrada
- **Optional Fields**: Campos opcionais para updates
- **Type Hints**: Tipagem que ajuda no desenvolvimento

### 🏗️ **Arquitetura de Software**
- **Separação de Responsabilidades**: Models, Routes, CRUD separados
- **Clean Code**: Código limpo e bem documentado
- **Error Handling**: Tratamento adequado de erros

### 🧪 **Testes Automatizados**
- **Test Client**: Como testar APIs com FastAPI
- **Fixtures**: Reutilização de código de teste
- **Mocking**: Simulação de dependências

## 🌱 Próximos passos no meu aprendizado

Agora que dominei o básico, quero evoluir para:

- [ ] **Autenticação JWT**: Aprender sobre segurança em APIs
- [ ] **Banco de Dados Real**: Dominar SQLAlchemy e migrations
- [ ] **Deploy na Nuvem**: Colocar a API no ar (Heroku, Railway)
- [ ] **Docker**: Containerização da aplicação
- [ ] **CI/CD**: Automatizar testes e deploy
- [ ] **Frontend**: Criar uma interface para a API

## 🤝 Quer aprender junto comigo?

Se você também está estudando FastAPI, fique à vontade para:

- 🍴 **Fork** este projeto e fazer suas próprias modificações
- 🐛 **Reportar bugs** ou sugerir melhorias
- 💡 **Compartilhar ideias** de novas funcionalidades
- ⭐ **Dar uma estrela** se o projeto te ajudou a aprender!

## 📫 Vamos trocar uma ideia?

Estou sempre aberto para conversar sobre programação e aprendizado!

- 📧 **Email**: pedrolv.fsilva@gmail.com
- 💼 **LinkedIn**: [Pedro Vergueiro](https://www.linkedin.com/in/pedro-vergueiro)
- 🌐 **GitHub**: [@pedrovergueiro](https://github.com/pedrovergueiro)

---

<div align="center">

**⭐ Se este projeto te inspirou a aprender FastAPI, dê uma estrela! ⭐**

*"A melhor forma de aprender é ensinando e compartilhando conhecimento"*

Feito com ❤️ e muito ☕ por Pedro Vergueiro | Estudante de Engenharia de Software

</div>

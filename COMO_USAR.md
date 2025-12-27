# 🚀 Como Usar a Task API

## ✅ Versão Funcionando

A API está funcionando! Use a **versão simples** que está 100% operacional.

### 🏃‍♂️ Para Rodar a API

```bash
# 1. Entre na pasta do projeto
cd task-api-fastapi

# 2. Entre na pasta app
cd app

# 3. Inicie o servidor
uvicorn main_simple:app --reload
```

### 🌐 Acessar a API

- **Documentação**: http://localhost:8000/docs
- **API**: http://localhost:8000/
- **Documentação alternativa**: http://localhost:8000/redoc

## 📝 Testando a API

### 1. Criar uma tarefa
```bash
curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar FastAPI",
    "description": "Ler documentação e praticar"
  }'
```

### 2. Ver todas as tarefas
```bash
curl -X GET "http://localhost:8000/tasks/"
```

### 3. Marcar como concluída
```bash
curl -X PATCH "http://localhost:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```

### 4. Deletar tarefa
```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

## 📁 Arquivos Importantes

### Versão Funcionando (Simples)
- `main_simple.py` - Aplicação principal
- `routes_simple.py` - Rotas da API
- `crud_simple.py` - Operações no "banco"
- `models_simple.py` - Modelos de dados
- `schemas.py` - Validação de dados

### Versão com SQLModel (Em desenvolvimento)
- `main.py` - Versão com banco SQLite
- `routes.py` - Rotas com banco
- `crud.py` - CRUD com SQLModel
- `models.py` - Modelos SQLModel
- `database.py` - Configuração do banco

## 🎯 Próximos Passos

1. **Usar a versão simples** para aprender FastAPI
2. **Estudar SQLModel** para implementar banco de dados real
3. **Adicionar autenticação** para usuários
4. **Deploy na nuvem** (Heroku, Railway, etc.)

## 🐛 Problemas Conhecidos

- A versão com SQLModel tem problemas de compatibilidade
- Os testes precisam ser ajustados para a versão simples
- A versão simples perde dados quando reinicia (usa memória)

## 💡 Dicas

- Use a documentação em `/docs` para testar a API
- A versão simples é perfeita para aprender
- Todos os dados ficam na memória (reiniciar = perder dados)
- O código está bem comentado para facilitar o aprendizado
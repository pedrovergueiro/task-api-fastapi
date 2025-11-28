🌟 TaskMaster – Aplicação de Gerenciamento de Tarefas (FastAPI + SQLModel + TailwindCSS)

Este repositório contém o TaskMaster, uma aplicação simples, direta e totalmente funcional para gerenciamento de tarefas.
Desenvolvi este projeto com o objetivo de praticar FastAPI, SQLModel e a integração entre um backend moderno e um frontend leve utilizando TailwindCSS.

O foco foi construir algo limpo, organizado e com uma arquitetura que represente o fluxo real de um projeto backend profissional.

🚀 Visão Geral do Projeto

O TaskMaster permite:

Criar tarefas

Listar todas as tarefas cadastradas

Editar tarefas existentes

Excluir tarefas

Visualizar tudo em uma interface simples desenvolvida com HTML + TailwindCSS

Consumir uma API REST construída com FastAPI

Apesar de ser um projeto simples, ele implementa boas práticas como:

✔ Separação de responsabilidades
✔ Organização em módulos
✔ Documentação automática da API
✔ Persistência em banco SQLite
✔ Comunicação clara entre Front ↔ Backend

🛠️ Tecnologias Utilizadas
🔹 Backend

FastAPI – Framework moderno, rápido e intuitivo para criação de APIs

SQLModel – ORM criado pelo autor do FastAPI, unindo Pydantic + SQLAlchemy

SQLite – Banco relacional leve e embutido

Uvicorn – Servidor ASGI rápido para rodar o projeto

🔹 Frontend

HTML5 – Estrutura base da interface

TailwindCSS (CDN) – Framework utilitário para estilização rápida e organizada

Fetch API – Comunicação entre frontend e backend

📂 Arquitetura do Projeto
taskmaster/
│── app/
│   ├── main.py        → inicialização da API e carregamento das rotas
│   ├── database.py    → criação do banco e conexão
│   ├── models.py      → modelos SQLModel (schema + tabela)
│   ├── routes.py      → rotas da API (CRUD)
│── frontend/
│   └── index.html     → página web com Tailwind consumindo a API
│── README.md


A estrutura foi pensada para deixar o projeto organizado, escalável e fácil de entender para recrutadores e outros devs.

⚙️ Como Executar o Projeto
1. Instale as dependências
pip install fastapi uvicorn sqlmodel sqlalchemy

2. Rode o servidor
uvicorn app.main:app --reload


A API ficará disponível em:

👉 http://127.0.0.1:8000

Documentação interativa do Swagger:

👉 http://127.0.0.1:8000/docs

🖥️ Como Abrir o Frontend

No navegador, basta abrir:

frontend/index.html


Ele já está configurado para comunicar com a API automaticamente.

🔌 Endpoints Implementados
Método	Rota	Descrição
GET	/tasks/	Lista todas as tarefas
POST	/tasks/	Cria uma nova tarefa
PUT	/tasks/{id}	Atualiza uma tarefa existente
DELETE	/tasks/{id}	Remove uma tarefa do banco

Exemplo de criação de tarefa:

{
  "title": "Estudar Python",
  "description": "Aprofundar SQLModel e FastAPI"
}

🎨 Frontend com TailwindCSS

A interface foi construída de forma simples e funcional, usando TailwindCSS via CDN para:

Layout responsivo

Botões estilizados

Cards de tarefas

Feedback visual rápido

O objetivo foi deixar limpo, minimalista e fácil de navegar, sem complicação.

🎯 Objetivo do Projeto

Este projeto foi criado para:

Reforçar conhecimentos em FastAPI

Aprender SQLModel e persistência de dados

Modelar uma API real com CRUD completo

Praticar integração entre frontend e backend

Criar algo profissional para compor meu portfólio no GitHub

📄 Licença

Projeto livre para estudo e evolução.
# Controle Financeiro API

API REST para controle financeiro pessoal, desenvolvida com **FastAPI**, com foco em **CRUD de lançamentos financeiros**, **validação de dados** e boas práticas de desenvolvimento de APIs REST.

O projeto permite criar, listar, atualizar e remover lançamentos financeiros (receitas e despesas), simulando o backend de um sistema real.

## Objetivos do Projeto

- Praticar o desenvolvimento de APIs REST com FastAPI  
- Implementar operações CRUD  
- Aplicar validação de dados com Pydantic  
- Organizar um projeto backend simples para portfólio  

## Tecnologias Utilizadas

- Python 3  
- FastAPI  
- Pydantic  
- Uvicorn  

## Funcionalidades

- Criar lançamentos financeiros  
- Listar lançamentos  
- Atualizar lançamento por ID  
- Remover lançamento por ID  
- Validação automática de dados  

## Estrutura do Projeto

controle-financeiro-api/  
├── app.py  
└── README.md  

## Como executar o projeto

1. Clonar o repositório  
git clone https://github.com/SEU_USUARIO/controle-financeiro-api.git  
cd controle-financeiro-api  

2. Criar ambiente virtual  
python3 -m venv venv  
source venv/bin/activate  

3. Instalar dependências  
pip install fastapi uvicorn  

4. Executar a aplicação  
python -m uvicorn app:app --reload  

5. Acessar a documentação  
Swagger UI disponível em: http://127.0.0.1:8000/docs  

## Endpoints Disponíveis

- GET /lancamentos  
- POST /lancamentos  
- PUT /lancamentos/{id}  
- DELETE /lancamentos/{id}  

## Primeiro commit (importante)

git status  
git add .  
git commit -m "Projeto inicial: API de controle financeiro com FastAPI"  

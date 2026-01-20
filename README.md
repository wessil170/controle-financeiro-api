# Controle Financeiro API

API REST simples para controle financeiro, desenvolvida com FastAPI.
O projeto permite criar, listar, atualizar e remover lançamentos financeiros
(receitas e despesas).

## Tecnologias utilizadas

- Python 3
- FastAPI
- Pydantic
- Uvicorn

## Funcionalidades

- Criar lançamento financeiro
- Listar lançamentos
- Atualizar lançamento por ID
- Remover lançamento por ID
- Validação de dados

## Estrutura do projeto

controle-financeiro-api/
├── app.py
└── README.md


## Como executar o projeto

### 1. Clonar o repositório
```bash
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
http://127.0.0.1:8000/docs
Exemplos de endpoints

GET /lancamentos

POST /lancamentos

PUT /lancamentos/{id}

DELETE /lancamentos/{id}


Salve.

---

## 6️⃣ Primeiro commit (importante)

```bash
git status
git add .
git commit -m "Projeto inicial: API de controle financeiro com FastAPI"

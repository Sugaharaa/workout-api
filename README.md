# 🏋️ Workout API

API desenvolvida como desafio de projeto da Digital Innovation One (DIO), utilizando FastAPI, SQLAlchemy, PostgreSQL, Alembic e Docker.

O projeto permite cadastrar e consultar atletas, categorias e centros de treinamento, trabalhando conceitos como APIs REST, validação de dados, banco de dados relacional, migrations, tratamento de exceções, filtros e paginação.

## 🚀 Tecnologias

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- asyncpg
- Alembic
- Docker
- fastapi-pagination

## 📁 Estrutura do projeto

```text
workout_api/
├── alembic/
│   └── versions/
├── atleta/
│   ├── controller.py
│   ├── models.py
│   └── schemas.py
├── categorias/
│   ├── controller.py
│   ├── models.py
│   └── schemas.py
├── centro_treinamento/
│   ├── controller.py
│   ├── models.py
│   └── schemas.py
├── contrib/
│   ├── repository/
│   ├── models.py
│   └── schemas.py
└── main.py
```

## ⚙️ Funcionalidades

A API possui funcionalidades para:

- cadastrar e consultar categorias;
- cadastrar e consultar centros de treinamento;
- cadastrar e consultar atletas;
- relacionar atletas com categorias e centros de treinamento;
- filtrar atletas por nome;
- filtrar atletas por CPF;
- retornar dados customizados no endpoint de atletas;
- tratar erros de integridade do banco;
- impedir cadastro duplicado de CPF;
- utilizar paginação com `limit` e `offset`.

## 🔎 Filtros

O endpoint de atletas aceita filtros através de query parameters.

Exemplo por nome:

```http
GET /atletas/?nome=João
```

Exemplo por CPF:

```http
GET /atletas/?cpf=12345678911
```

## 📄 Paginação

A listagem de atletas utiliza `fastapi-pagination`.

Exemplo:

```http
GET /atletas/?limit=10&offset=0
```

A resposta contém os registros encontrados e informações da paginação.

## ⚠️ Tratamento de erros

O projeto trata erros de integridade utilizando:

```python
sqlalchemy.exc.IntegrityError
```

Por exemplo, ao tentar cadastrar um atleta com um CPF já existente, a API retorna status HTTP `303` e uma mensagem informando que o atleta já está cadastrado.

## 🐳 Banco de dados

O PostgreSQL pode ser executado utilizando Docker Compose:

```bash
docker compose up -d
```

## 🔐 Variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`.

Exemplo:

```env
POSTGRES_USER=workout
POSTGRES_PASSWORD=workout
POSTGRES_DB=workout
POSTGRES_HOST=localhost
POSTGRES_PORT=5433

DATABASE_URL=postgresql+asyncpg://workout:workout@localhost:5433/workout
```

O arquivo `.env` não deve ser enviado ao repositório.

## 📦 Instalação

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente e instale as dependências:

```bash
pip install -r requirements.txt
```

Suba o PostgreSQL:

```bash
docker compose up -d
```

Execute as migrations:

```bash
alembic upgrade head
```

Inicie a API:

```bash
uvicorn workout_api.main:app --reload
```

## 📚 Documentação

Com a aplicação executando, a documentação Swagger pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

## 🎯 Desafio

Projeto desenvolvido como parte de um desafio prático da Digital Innovation One, aplicando conceitos de desenvolvimento de APIs com FastAPI e persistência de dados utilizando PostgreSQL e SQLAlchemy.

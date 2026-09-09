# 📚 StudyManager API

> **API RESTful completa para gerenciamento de Usuários, Cursos e Matrículas**, desenvolvida aplicando **Arquitetura Limpa (Clean Architecture)**, **Princípios de Clean Code**, **ORM SQLAlchemy 2.0**, validação com **Pydantic v2** e padronização global de respostas HTTP.

---

## 🏛️ Estrutura de Pastas e Arquitetura Limpa

```
API_Projeto/
├── app/
│   ├── core/
│   │   ├── config.py              # Configurações globais e variáveis de ambiente
│   │   └── exceptions.py          # Exceções customizadas de domínio (404, 409, 422)
│   ├── domain/                    # Camada Central: Regras e entidades de negócio puras
│   │   ├── entities/              # Entidades desacopladas de frameworks e ORM
│   │   │   ├── user.py
│   │   │   ├── course.py
│   │   │   └── enrollment.py
│   │   └── repositories/          # Interfaces abstratas de persistência (Contratos)
│   │       ├── user_repository.py
│   │       ├── course_repository.py
│   │       └── enrollment_repository.py
│   ├── use_cases/                 # Casos de Uso: Orquestração e regras da aplicação (SRP)
│   │   ├── user/                  # Casos de uso de Usuários
│   │   │   ├── create_user.py
│   │   │   ├── list_users.py
│   │   │   ├── get_user.py
│   │   │   ├── update_user.py
│   │   │   ├── delete_user.py
│   │   │   └── get_user_courses.py
│   │   ├── course/                # Casos de uso de Cursos
│   │   │   ├── create_course.py
│   │   │   ├── list_courses.py
│   │   │   ├── get_course.py
│   │   │   ├── update_course.py
│   │   │   └── delete_course.py
│   │   └── enrollment/            # Casos de uso de Matrículas
│   │       └── create_enrollment.py
│   ├── infrastructure/            # Camada de Infraestrutura: Detalhes de I/O e Banco
│   │   ├── database/
│   │   │   ├── session.py         # Conexão, engine e SessionFactory do SQLAlchemy
│   │   │   └── models.py          # Modelos ORM e mapeamento relacional de tabelas
│   │   └── repositories/          # Implementações concretas das interfaces de repositório
│   │       ├── user_repository_impl.py
│   │       ├── course_repository_impl.py
│   │       └── enrollment_repository_impl.py
│   └── presentation/              # Camada de Apresentação: Controladores HTTP e Schemas
│       ├── schemas/               # Schemas Pydantic (Validação e DTOs de I/O)
│       │   ├── common.py          # Envelope padronizado de resposta ({success, message, data})
│       │   ├── user_schema.py
│       │   ├── course_schema.py
│       │   └── enrollment_schema.py
│       ├── controllers/           # Controladores/Rotas FastAPI (sem regras de negócio)
│       │   ├── user_controller.py
│       │   ├── course_controller.py
│       │   └── enrollment_controller.py
│       ├── middleware/
│       │   └── error_handler.py   # Manipulador global de erros e padronização JSON
│       └── dependencies.py        # Provedores de injeção de dependência (DI)
├── tests/                         # Suíte de testes automatizados com Pytest
│   ├── conftest.py                # Fixtures e banco SQLite isolado em memória
│   ├── test_users.py              # Testes do CRUD de Usuários e validações
│   ├── test_courses.py            # Testes do CRUD de Cursos
│   └── test_enrollments.py        # Testes de Matrículas e Consultas Relacionais
├── Activity.md                    # Especificação original do projeto
├── pytest.ini                     # Configuração do Pytest
├── requirements.txt               # Dependências do projeto
├── run.py                         # Script de inicialização do servidor
├── .env.example                   # Exemplo de variáveis de ambiente
└── .gitignore                     # Arquivos ignorados pelo Git
```

### 🎯 Justificativa da Organização (Arquitetura Limpa)
> A estrutura adota rigorosamente os preceitos da **Arquitetura Limpa (Clean Architecture)** ao isolar as regras de negócio centrais (`domain` e `use_cases`) de quaisquer tecnologias externas e bibliotecas de entrega HTTP (`presentation`) ou mecanismos de banco de dados (`infrastructure`). Os controladores HTTP atuam como meros adaptadores de entrada sem lógica de negócio embutida, delegando cada operação para um caso de uso específico com responsabilidade única (SRP), enquanto o acesso aos dados é realizado por contratos abstratos de repositório implementados via SQLAlchemy 2.0 com injeção de dependências nativa do FastAPI, assegurando alta testabilidade, manutenibilidade e total conformidade com os princípios SOLID e Clean Code.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.14+
- **Framework Web**: FastAPI (v0.115+)
- **Servidor ASGI**: Uvicorn
- **ORM**: SQLAlchemy 2.0 (com tipagem estática e suporte a `Mapped` / `mapped_column`)
- **Validação de Dados**: Pydantic v2 (com `EmailStr` e `ConfigDict`)
- **Banco de Dados**: SQLite (com constraints e chaves estrangeiras ativadas)
- **Testes Automatizados**: Pytest + HTTPX

---

## 🚀 Como Executar o Projeto

### 1. Clonar o Repositório e Acessar a Pasta
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd API_Projeto
```

### 2. Criar e Ativar o Ambiente Virtual
**No Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**No Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Iniciar o Servidor
```bash
py run.py
# Ou alternativamente:
# uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

O servidor estará disponível em: **`http://127.0.0.1:8000`**

---

## 📖 Documentação Interativa da API (Swagger / ReDoc)

Com o servidor em execução, acesse no navegador:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Como Executar os Testes Automatizados

A suíte de testes cobre 100% dos fluxos solicitados (CRUDs, validações de integridade, e-mail único, carga horária positiva, prevenção de matrículas duplicadas e consultas relacionais):

```bash
pytest -v
```

---

## 📋 Endpoints Disponíveis

Todas as respostas seguem o envelope JSON padronizado:
```json
{
  "success": true,
  "message": "Mensagem informativa",
  "data": { ... }
}
```

### 👤 Usuários (`/users`)

| Método | Endpoint | Descrição | Status de Sucesso |
|---|---|---|---|
| `POST` | `/users` | Cadastra novo usuário (e-mail único obrigatório) | `201 Created` |
| `GET` | `/users` | Lista todos os usuários cadastrados | `200 OK` |
| `GET` | `/users/{id}` | Retorna detalhes de um usuário por ID | `200 OK` |
| `PUT` | `/users/{id}` | Atualiza nome e/ou e-mail de um usuário | `200 OK` |
| `DELETE` | `/users/{id}` | Exclui usuário e suas matrículas associadas | `200 OK` |
| `GET` | `/users/{id}/courses` | **Consulta Relacional**: Retorna o usuário e a lista de cursos em que está matriculado | `200 OK` |

### 📘 Cursos (`/courses`)

| Método | Endpoint | Descrição | Status de Sucesso |
|---|---|---|---|
| `POST` | `/courses` | Cadastra novo curso (`workload > 0`) | `201 Created` |
| `GET` | `/courses` | Lista todos os cursos cadastrados | `200 OK` |
| `GET` | `/courses/{id}` | Retorna detalhes de um curso por ID | `200 OK` |
| `PUT` | `/courses/{id}` | Atualiza informações de um curso | `200 OK` |
| `DELETE` | `/courses/{id}` | Exclui curso e suas matrículas associadas | `200 OK` |

### 📝 Matrículas (`/enrollments`)

| Método | Endpoint | Descrição | Status de Sucesso |
|---|---|---|---|
| `POST` | `/enrollments` | Matricula um usuário em um curso (impede duplicidades e valida existência) | `201 Created` |

---

## 💡 Exemplos de Requisições com cURL

### 1. Criar Usuário
```bash
curl -X POST "http://127.0.0.1:8000/users" \
  -H "Content-Type: application/json" \
  -d '{"name": "Maria Silva", "email": "maria.silva@email.com"}'
```

### 2. Criar Curso
```bash
curl -X POST "http://127.0.0.1:8000/courses" \
  -H "Content-Type: application/json" \
  -d '{"title": "Arquitetura Limpa com Python", "description": "Curso completo de Clean Architecture", "workload": 40}'
```

### 3. Matricular Usuário no Curso
```bash
curl -X POST "http://127.0.0.1:8000/enrollments" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "course_id": 1}'
```

### 4. Consultar Cursos do Usuário (Relacionamento ORM)
```bash
curl -X GET "http://127.0.0.1:8000/users/1/courses"
```
**Exemplo de Resposta:**
```json
{
  "success": true,
  "message": "User courses retrieved successfully",
  "data": {
    "user": {
      "id": 1,
      "name": "Maria Silva",
      "email": "maria.silva@email.com",
      "created_at": "2026-09-09T09:00:00Z"
    },
    "courses": [
      {
        "id": 1,
        "title": "Arquitetura Limpa com Python",
        "description": "Curso completo de Clean Architecture",
        "workload": 40
      }
    ]
  }
}
```

### 5. Exemplo de Resposta de Erro Padronizada (409 Conflict - Matrícula Duplicada)
```json
{
  "success": false,
  "message": "User 1 is already enrolled in course 'Arquitetura Limpa com Python' (ID 1).",
  "data": null
}
```

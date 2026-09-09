🎯 Objetivo
Desenvolver uma API RESTful completa, aplicando:

Conceitos de Arquitetura Limpa

Princípios de Clean Code

Uso de ORM

Tratamento adequado de erros

🏗️ Contexto do Projeto
Você foi contratado para desenvolver a API de um sistema chamado:

📚 StudyManager API
Uma API responsável pelo gerenciamento de:

Usuários

Cursos

Matrículas

A aplicação deverá permitir:

Cadastro de usuários

Cadastro de cursos

Matrícula de usuários em cursos

Consulta de dados

Atualização e exclusão de registros

⚙️ Tecnologias Permitidas (escolha uma)
🐍 FastAPI + SQLAlchemy

🟢 Express + Prisma ou Sequelize

🔴 Laravel + Eloquent ORM

📌 PARTE 1 – Modelagem e Estrutura
1️⃣ Modelagem do Banco
Crie as seguintes entidades:

👤 User
id

name

email (único)

created_at

📘 Course
id

title

description

workload (em horas)

📝 Enrollment
id

user_id

course_id

enrolled_at

📌 Relacionamentos:

Um usuário pode ter várias matrículas

Um curso pode ter várias matrículas

Uma matrícula pertence a um usuário e a um curso

2️⃣ Estrutura baseada em Arquitetura Limpa
Organize o projeto separando camadas, por exemplo:

controllers / routes

usecases / services

repositories

entities / models

infrastructure (ORM, banco)

📌 Entregar:

Estrutura de pastas

Explicação breve (1 parágrafo) justificando a organização

📌 PARTE 2 – Implementação da API
3️⃣ CRUD de Usuário
Endpoints obrigatórios:

POST /users

GET /users

GET /users/{id}

PUT /users/{id}

DELETE /users/{id}

Regras:

Email deve ser único

Validação de dados obrigatória

4️⃣ CRUD de Cursos
Mesmo padrão de endpoints.

5️⃣ Matrículas
Criar endpoint:

POST /enrollments

Regras:

Não permitir matrícula duplicada

Validar se usuário e curso existem

6️⃣ Consulta Relacional
Criar endpoint:

GET /users/{id}/courses

Retornar:

Dados do usuário

Lista de cursos em que está matriculado

(Deve usar ORM com relacionamento adequado)

📌 PARTE 3 – Clean Code e Boas Práticas
7️⃣ Aplicação de Clean Code
Critérios avaliados:

Nomes claros e significativos

Métodos curtos

Separação de responsabilidades

Ausência de lógica de negócio no controller

Tratamento adequado de exceções

Base conceitual recomendada:

📘 Clean Code – de Robert C. Martin

8️⃣ Padronização de Respostas
A API deve:

Retornar códigos HTTP corretos

Padronizar mensagens de erro

Utilizar JSON consistente

Exemplo:

```json
{
  "success": false,
  "message": "User not found",
  "data": null
}
```

📂 Estrutura Esperada
Os alunos deverão entregar:

🔹 Repositório no GitHub:
🔗 Link Projeto no gitHub

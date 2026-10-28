# 📘 Atividade: Construindo REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a construir uma REST API usando o framework FastAPI, criando endpoints para gerenciar uma lista de tarefas (to-do list) com operações de leitura, criação, atualização e remoção.

## 📝 Tarefas

### 🛠️ Criar o Primeiro Endpoint

#### Descrição
Use o código inicial para criar sua primeira API com FastAPI. Implemente um endpoint raiz que retorne uma mensagem de boas-vindas e execute o servidor localmente com `uvicorn`.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI`
- Implementar um endpoint `GET /` que retorne `{"message": "Welcome to the To-Do API"}`
- Executar com `uvicorn main:app --reload` e responder corretamente em `http://localhost:8000`


### 🛠️ Listar e Buscar Tarefas

#### Descrição
Implemente endpoints de leitura para a lista de tarefas armazenada em memória. Os estudantes devem usar path parameters para buscar uma tarefa específica pelo seu `id`.

#### Requisitos
O programa concluído deve:

- Implementar `GET /todos` que retorne a lista completa de tarefas
- Implementar `GET /todos/{todo_id}` que retorne a tarefa com o `id` informado
- Retornar erro `404` com `HTTPException` quando a tarefa não existir


### 🛠️ Criar Tarefas com Pydantic

#### Descrição
Adicione um endpoint para criar novas tarefas, usando um modelo Pydantic para validar os dados enviados no corpo da requisição.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic `TodoItem` com os campos `title` (str) e `completed` (bool, padrão `False`)
- Implementar `POST /todos` que receba um `TodoItem`, gere um `id` automaticamente e adicione a tarefa à lista
- Retornar a tarefa criada (incluindo o `id`) com status code `201`


### 🛠️ Completar o CRUD

#### Descrição
Finalize a API implementando os endpoints de atualização e remoção de tarefas, completando todas as operações CRUD (Create, Read, Update, Delete).

#### Requisitos
O programa concluído deve:

- Implementar `PUT /todos/{todo_id}` que atualize o `title` e o `completed` de uma tarefa existente
- Implementar `DELETE /todos/{todo_id}` que remova a tarefa da lista
- Retornar erro `404` em ambos os endpoints quando a tarefa não existir
- Ser testável pela documentação interativa em `http://localhost:8000/docs`

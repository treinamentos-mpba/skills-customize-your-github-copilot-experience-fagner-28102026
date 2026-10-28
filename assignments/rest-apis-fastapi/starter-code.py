# Código Inicial para a Atividade de REST APIs com FastAPI
#
# Instalação das dependências:
#   pip install fastapi uvicorn
#
# Para executar o servidor:
#   uvicorn main:app --reload
#
# Documentação interativa disponível em: http://localhost:8000/docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="To-Do API")

# "Banco de dados" em memória para as tarefas
todos = [
    {"id": 1, "title": "Estudar FastAPI", "completed": False},
    {"id": 2, "title": "Fazer a lição de casa", "completed": True},
]

# Tarefa 1: Criar o Primeiro Endpoint
# Implemente o endpoint GET / que retorna uma mensagem de boas-vindas


# Tarefa 2: Listar e Buscar Tarefas
# Implemente GET /todos e GET /todos/{todo_id}
# Dica: use HTTPException(status_code=404, detail="...") quando a tarefa não existir


# Tarefa 3: Criar Tarefas com Pydantic
# Defina o modelo TodoItem abaixo e implemente POST /todos

class TodoItem(BaseModel):
    # Defina os campos: title (str) e completed (bool, padrão False)
    pass


# Tarefa 4: Completar o CRUD
# Implemente PUT /todos/{todo_id} e DELETE /todos/{todo_id}

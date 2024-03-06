from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# Criar conexão com o banco de dados SQLite
conn = sqlite3.connect('../data/projeto.db')
cur = conn.cursor()

app = FastAPI()

class Item(BaseModel):
    nome: str
    lote: int
    validade: int
    imagem: str

# Rota para obter todos os itens
@app.get("/itens/")
async def get_usuarios():
    cur.execute("SELECT * FROM item")
    itens = cur.fetchall()
    return itens

@app.get("/carrinhos/")
async def get_usuarios():
    cur.execute("SELECT * FROM carrinho")
    itens = cur.fetchall()
    return itens

@app.post("/adicionar_itens/")
async def criar_usuario(Item:Item):
    cur.execute("INSERT INTO item (nome, lote, validade, imagem) VALUES (?, ?,?,?)", (Item.nome,Item.lote,Item.validade,Item.imagem))
    conn.commit()
    return {"status": "Usuário criado com sucesso"}
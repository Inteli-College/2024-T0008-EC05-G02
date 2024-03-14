from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# Criar conexão com o banco de dados SQLite
conn = sqlite3.connect('../data/projeto.db')
cur = conn.cursor()

app = FastAPI()

class Item(BaseModel):
    item_id : int
    id_operacao: int
    nome: str
    lote: int
    validade: int
    imagem: str

class Operacao(BaseModel):
    id: int
    responsavel: str
    data: int
    id_carrinho: int
    tipo: int

# Rota para obter todos os itens
@app.get("/itens/")
async def get_usuarios():
    cur.execute("SELECT * FROM itens")
    itens = cur.fetchall()
    return itens

@app.get("/operacoes/")
async def get_usuarios():
    cur.execute("SELECT * FROM operacoes")
    itens = cur.fetchall()
    return itens

@app.post("/adicionar_item/")
async def criar_usuario(Item:Item):
    cur.execute("INSERT INTO itens (item_id,nome, lote, validade, imagem, id_operacao) VALUES (?,?,?,?,?,?)", (Item.item_id,Item.nome,Item.lote,Item.validade,Item.imagem, Item.id_operacao))
    conn.commit()
    return {"status": "Usuário criado com sucesso"}

@app.post("/adicionar_operacao/")
async def criar_usuario(Operacao: Operacao):
    cur.execute("INSERT INTO operacao (id, responsavel, data, id_carrinho, tipo) VALUES (?,?,?,?,?)", (Operacao.id,Operacao.data,Operacao.responsavel,Operacao.id_carrinho, Operacao.tipo))
    conn.commit()
    return {"status": "Usuário criado com sucesso"}
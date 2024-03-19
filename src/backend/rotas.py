from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# Criar conexão com o banco de dados SQLite
conn = sqlite3.connect('../data/ad_alma.db')
cur = conn.cursor()

app = FastAPI()

class Bipagem(BaseModel):
    id_item : int
    id_operacao: int
    nome: str
    lote: int
    validade: int
    fornecedor: str

class Operacao(BaseModel):
    id: int
    id_responsavel: int
    id_carrinho: int
    data: int
    tipo: str

class Carrinho(BaseModel):
    id: int
    car_layout: int

# Rota para obter todos os itens
@app.get("/bipagem/")
async def get_usuarios():
    cur.execute("SELECT * FROM bipagem")
    bipagem = cur.fetchall()
    return bipagem

@app.get("/operacoes/")
async def get_usuarios():
    cur.execute("SELECT * FROM operacoes")
    operacoes = cur.fetchall()
    return operacoes

@app.get("/carrinhos/")
async def get_usuarios():
    cur.execute("SELECT * FROM carrinhos")
    carrinhos = cur.fetchall()
    return carrinhos

@app.post("/adicionar_bipagem/")
async def criar_usuario(Bipagem: Bipagem):
    cur.execute("INSERT INTO Bipagem (id_item,nome, lote, validade, fornecedor, id_operacao) VALUES (?,?,?,?,?,?)", (Bipagem.id_item,Bipagem.nome,Bipagem.lote,Bipagem.validade,Bipagem.fornecedor, Bipagem.id_operacao))
    conn.commit()
    return {"status": "Bipagem adicionada com sucesso"}

@app.post("/adicionar_operacao/")
async def criar_usuario(Operacao: Operacao):
    cur.execute("INSERT INTO operacoes (id, data, id_responsavel, id_carrinho, tipo) VALUES (?,?,?,?,?)", (Operacao.id,Operacao.data,Operacao.id_responsavel,Operacao.id_carrinho, Operacao.tipo))
    conn.commit()
    return {"status": "Operação adicionada com sucesso"}

@app.post("/adicionar_carrinho/")
async def criar_usuario(Carrinho: Carrinho):
    cur.execute("INSERT INTO carrinhos (id, car_layout) VALUES (?,?)", (Carrinho.id,Carrinho.car_layout))
    conn.commit()
    return {"status": "Carrinho adicionado com sucesso"}

# Deleção do carrinho
@app.delete("/deletar_carrinho/{id}")
async def deletar_usuario(id: int):
    cur.execute("DELETE FROM carrinhos WHERE id=?", (id,))
    conn.commit()
    return {"status": "Carrinho deletado com sucesso"}

# Atualização de carrinho
@app.post("/atualizar_carrinho/")
async def atualizar_usuario(Carrinho: Carrinho):
    cur.execute("UPDATE carrinhos SET car_layout=? WHERE id=?", (Carrinho.car_layout, Carrinho.id))
    conn.commit()
    return {"status": "Carrinho atualizado com sucesso"}

# Atualização da bipagem no reabastecimento
@app.post("/atualizar_bipagem/")
async def atualizar_usuario(Bipagem: Bipagem):
    cur.execute("UPDATE Bipagem SET id_item=?,nome=?,lote=?,validade=?,fornecedor=? WHERE id_operacao=?", (Bipagem.id_item,Bipagem.nome,Bipagem.lote,Bipagem.validade,Bipagem.fornecedor, Bipagem.id_operacao))
    conn.commit()
    return {"status": "Bipagem atualizada com sucesso"}
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import uvicorn
import datetime
from typing import List, Optional



# Criar conexão com o banco de dados SQLite
conn = sqlite3.connect('../data/ad_alma.db')
cur = conn.cursor()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Bipagem(BaseModel):
    id_item : int
    id_operacao: int
    nome: str
    lote: str
    validade: str
    fornecedor: str

class Operacao(BaseModel):
    id_operacao: Optional[int] = None
    id_responsavel: int
    id_carrinho: int
    data: str
    tipo_operacao: str
    tipo_carrinho: str

class Carrinho(BaseModel):
    id: int
    car_layout: int

# Rota para obter todos os itens    
@app.get("/bipagem/")
async def get_usuarios():
    cur.execute("SELECT * FROM bipagem")
    bipagem = cur.fetchall()
    return bipagem

@app.get("/item_informacao/{id_operacao}/{}")
async def get_bipagem(id_operacao: int):
    cur.execute("SELECT id, tipo_carrinho, tipo_operacao FROM operacoes WHERE id=?", (id_operacao,))
    operacao = cur.fetchone()
    # sql = f"SELECT nome, tipo_carrinho FROM operacoes INNER JOIN bipagem on bipagem.id_operacao = operacoes.id WHERE bipagem.id_operacao={id_operacao}"
    cur.execute("SELECT id_item, id_operacao, nome, lote, validade, fornecedor, tipo_carrinho, tipo_operacao FROM operacoes INNER JOIN bipagem on bipagem.id_operacao = operacoes.id WHERE bipagem.id_operacao=?", (id_operacao,))
    bipagem = cur.fetchall()
    bipagem_dict = []
    for row in bipagem:
        bipagem_dict.append({
            'id_item': row[0],
            'id_operacao': row[1],
            'nome': row[2],
            'lote': row[3],
            'validade': row[4],
            'fornecedor': row[5],
            'tipo_carrinho': row[6],
            'tipo_operacao': row[7]
        })
    return bipagem_dict

@app.get("/operacoes/", response_model=List[Operacao])
async def get_usuarios():
    cur.execute("SELECT * FROM operacoes")
    operacoes = cur.fetchall()
    # return [Operacao(**{field_name: value for field_name, value in zip(["id_responsavel", "id_carrinho", "data", "tipo_operacao", "tipo_carrinho"], operacao)}) for operacao in operacoes]
    print(operacoes)
    operacoes_formatted = []
    for operacao in operacoes:
        operacao_dict = {field_name: value for field_name, value in zip(["id_operacao", "id_responsavel", "data","id_carrinho", "tipo_operacao", "tipo_carrinho"], operacao)}
        operacao_dict['id_carrinho'] = int(operacao_dict['id_carrinho'])
        operacao_dict['data'] = str(operacao_dict['data'])
        operacao_dict['tipo_operacao'] = str(operacao_dict['tipo_operacao']) if operacao_dict['tipo_operacao'] is not None else ''
        operacao_dict['tipo_carrinho'] = str(operacao_dict['tipo_carrinho']) if operacao_dict['tipo_carrinho'] is not None else ''
        operacoes_formatted.append(Operacao(**operacao_dict))
    return operacoes_formatted

@app.get("/bipagem/{id_operacao}", response_model=List[Bipagem])
async def get_bipagem(id_operacao: int):
    cur.execute("SELECT * FROM bipagem WHERE id_operacao=?", (id_operacao,))
    bipagem_results = cur.fetchall()

    bipagem_formatted = []
    for bipagem_item in bipagem_results:
        bipagem_dict = {field_name: value for field_name, value in zip(["id_item", "nome", "lote", "validade", "dose" ,"fornecedor", "id_operacao"], bipagem_item)}
        
        bipagem_dict['id_operacao'] = int(bipagem_dict['id_operacao'])
        bipagem_dict['validade'] = str(bipagem_dict['validade'])  # Assuming it's a date field, you might want to format it.
        
        bipagem_formatted.append(Bipagem(**bipagem_dict))

    return bipagem_formatted

@app.get("/operacao/{id_operacao}")
async def get_operacao(id_operacao: int):
    cur.execute("SELECT * FROM operacoes WHERE id=?", (id_operacao,))
    operacao = cur.fetchone()
    if operacao is not None:
        return Operacao(**{field_name: value for field_name, value in zip(["id_operacao", "id_responsavel", "data","id_carrinho", "tipo_operacao", "tipo_carrinho"], operacao)})
    else:
        return None

@app.get("/carrinhos/")
async def get_usuarios():
    cur.execute("SELECT * FROM carrinhos")
    carrinhos = cur.fetchall()
    return carrinhos

@app.post("/adicionar_bipagem/")
async def criar_usuario(Bipagem: Bipagem):
    cur.execute("INSERT INTO bipagem (id_item,nome, lote, validade, fornecedor, id_operacao) VALUES (?,?,?,?,?,?)", (Bipagem.id_item,Bipagem.nome,Bipagem.lote,Bipagem.validade,Bipagem.fornecedor, Bipagem.id_operacao))
    conn.commit()
    return {"status": "Bipagem adicionada com sucesso"}

@app.post("/adicionar_operacao/")
async def criar_usuario(Operacao: Operacao):
    cur.execute("INSERT INTO operacoes (data, id_responsavel, id_carrinho, tipo_operacao, tipo_carrinho) VALUES (?,?,?,?,?)", (Operacao.data,Operacao.id_responsavel,Operacao.id_carrinho, Operacao.tipo_operacao, Operacao.tipo_carrinho))
    conn.commit()
    return {"status": "Operação adicionada com sucesso"}

@app.post("/adicionar_carrinho/")
async def criar_usuario(Carrinho: Carrinho):
    cur.execute("INSERT INTO carrinhos (id, car_layout) VALUES (?,?)", (Carrinho.id,Carrinho.car_layout))
    conn.commit()
    return {"status": "Carrinho adicionado com sucesso"}

@app.delete("/deletar_carrinho/")
async def deletar_usuario(Carrinho: Carrinho):
    cur.execute("DELETE FROM carrinhos WHERE id=?", (Carrinho.id,))
    conn.commit()
    return {"status": "Carrinho deletado com sucesso"}

@app.post("/atualizar_carrinho/")
async def atualizar_usuario(Carrinho: Carrinho):
    cur.execute("UPDATE carrinhos SET car_layout=? WHERE id=?", (Carrinho.car_layout, Carrinho.id))
    conn.commit()
    return {"status": "Carrinho atualizado com sucesso"}

@app.post("/atualizar_bipagem/")
async def atualizar_usuario(Bipagem: Bipagem):
    cur.execute("UPDATE bipagem SET id_item=?,nome=?,lote=?,validade=?,fornecedor=? WHERE id_operacao=?", (Bipagem.id_item,Bipagem.nome,Bipagem.lote,Bipagem.validade,Bipagem.fornecedor, Bipagem.id_operacao))
    conn.commit()
    return {"status": "Bipagem atualizada com sucesso"}

@app.post("/atualizar_operacao/")
async def atualizar_usuario(Operacao: Operacao):
    cur.execute("UPDATE operacoes SET id_responsavel=?,id_carrinho=?,data=?,tipo=? WHERE id=?", (Operacao.id_responsavel,Operacao.id_carrinho,Operacao.data,Operacao.tipo, Operacao.id))
    conn.commit()
    return {"status": "Operação atualizada com sucesso"}

# Rota indireta de teste
@app.delete("/deletar_operacao/")
async def deletar_usuario(Operacao: Operacao):
    cur.execute("DELETE FROM operacoes WHERE id=?", (Operacao.id,))
    conn.commit()
    return {"status": "Operação deletada com sucesso"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
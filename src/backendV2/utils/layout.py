import json
def load_data():
    with open('layouts.json', 'r') as file:
        data = json.load(file)
    return data

def percorrer_layout(layout_id):
    ponto1: tuple[float, float, float] = (182.11688232421875,-338.3886413574219,15.28591251373291) #VERTICE SUPERIOR ESQUERDO DA BANDEJA 
    ponto2: tuple[float, float, float] = (-82.36273956298828,-343.5843811035156,9.381065368652344) #VERTICE SUPERIOR DIREITO DA BANDEJA
    ponto3: tuple[float, float, float] = (188.03305053710938,-166.6496124267578,10.483986854553223) #VERTICE INFERIOR ESQUERDO DA BANDEJA
    ponto4: tuple[float, float, float] = (-74.89086151123047,-166.2255096435547,13.807846069335938)#VERTICE INFERIOR DIREITO DA BANDEJA

    length: float = ponto2[0] - ponto1[0] #COMPRIMENTO DA BANDEJA 
    height: float = ponto1[1] - ponto3[1] #ALTURA DA BANDEJA

def return_layout_by_id(id):
    dados = load_data()
    layout_especificado = next((layout for layout in dados['layouts'] if layout['id'] == id), None)
    return layout_especificado

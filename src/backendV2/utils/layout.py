import json
from os.path import join, dirname, realpath
import asyncio

def load_data(file_name: str):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def percorrer_layout(layout_id):
    ponto1: tuple[float, float, float] = (182.11688232421875,-338.3886413574219,15.28591251373291) #VERTICE SUPERIOR ESQUERDO DA BANDEJA  #type: ignore
    ponto2: tuple[float, float, float] = (-82.36273956298828,-343.5843811035156,9.381065368652344) #VERTICE SUPERIOR DIREITO DA BANDEJA
    ponto3: tuple[float, float, float] = (188.03305053710938,-166.6496124267578,10.483986854553223) #VERTICE INFERIOR ESQUERDO DA BANDEJA
    ponto4: tuple[float, float, float] = (-74.89086151123047,-166.2255096435547,13.807846069335938)#VERTICE INFERIOR DIREITO DA BANDEJA

    length: float = ponto2[0] - ponto1[0] #COMPRIMENTO DA BANDEJA 
    height: float = ponto1[1] - ponto3[1] #ALTURA DA BANDEJA



def return_layout_by_id(id):
    dados = load_data('layouts.json')
    layout_especificado = next((layout for layout in dados['layouts'] if layout['id'] == id), None)
    return layout_especificado

def find_medication_position(medication_name):
    stock_data = load_data('stock.json')
    medication = next((item for item in stock_data['stock'] if item['Nome'] == medication_name), None)
    return medication['Posicao'] if medication else None




if __name__ == '__main__':
    print(find_medication_position('dipirona'))

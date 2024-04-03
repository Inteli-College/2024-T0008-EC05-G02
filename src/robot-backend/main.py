from flask import Flask, jsonify, request
from functions import *
import json
import pydobot 
app = Flask(__name__)
def armazenar_layout_por_id(id_especificado):
    dados = carregar_dados()
    layout_especificado = next((layout for layout in dados['layouts'] if layout['id'] == id_especificado), None)
    return layout_especificado

def carregar_dados():
    with open('layouts.json', 'r') as file:
        dados = json.load(file)
    return dados

def bipar(x,robo):
    match(x):
        case 0:
            robo.move_to(239.0592498779297, -30.517675399780273, -1.8932082653045654,robo.r, wait=True)
            robo.suck(False)
        case 1:
            robo.move_to(138.08914184570312, 283.528076171875, 13.611610412597656,robo.r, wait=True)
            robo.suck(False)
        case _:
            print('Bipagem inválida')

@app.route("/")
def hello_world():
    return 'fodase'
@app.route('/home', methods=['GET'])
def returnhome():
    #return robo.origem_global()
    return None
@app.route('/move', methods=['POST'])
def move_to_specific():
    data = request.get_json()
    print(data)
    xaxis = data.get('xaxis')
    yaxis = data.get('yaxis')
    zaxis = data.get('zaxis')
    print(xaxis,yaxis,zaxis)
    return None
@app.get('/demonstracao')
def demonstracao():
    robo = pydobot.Dobot(port='COM10', verbose=False)
    ponto1 = (182.11688232421875,-338.3886413574219,15.28591251373291) #VERTICE SUPERIOR ESQUERDO DA BANDEJA 
    ponto2 = (-82.36273956298828,-343.5843811035156,9.381065368652344) #VERTICE SUPERIOR DIREITO DA BANDEJA
    ponto3 = (188.03305053710938,-166.6496124267578,10.483986854553223) #VERTICE INFERIOR ESQUERDO DA BANDEJA
    ponto4 = (-74.89086151123047,-166.2255096435547,13.807846069335938)#VERTICE INFERIOR DIREITO DA BANDEJA
    l = ponto2[0] - ponto1[0] #COMPRIMENTO DA BANDEJA 
    h = ponto1[1] - ponto3[1] #ALTURA DA BANDEJA
    print(h)
    print(l)
    base_url = 'http://127.0.0.1:5000/move'
    layoutInput = 'layout_01'
    if armazenar_layout_por_id(layoutInput) is not None:
        layout = armazenar_layout_por_id(layoutInput)
        print(layout['remedios'])
        count = len(layout['remedios'])
        x = ponto1[0]
        y = ponto1[1]
        z = ponto1[2]
        for i in layout['remedios']:
            robo.move_to(61.016326904296875, -238.06103515625, 164.80154418945312,robo.r,wait=True)
            print(f"remedio: {i}")
            print(count%layout['nc'])
            if count == len(layout['remedios']): # "Caso base" entre MUITAS ASPAS
                x += l/(layout['nc'] *2)
                base = x
                y -= h/(layout['nl'] * 2)
                print('primeira operação')
                print(f'coordenadas:{(x,y)}')
                obj = {"xaxis": x,
                        "yaxis": y,
                        "zaxis": z}
            #requests.post(base_url,json = obj)
                robo.move_to(x,y,z,robo.r,wait=True)
                robo.move_to(x,y,-19.2,robo.r,wait=True)
                robo.suck(True)
                robo.move_to(159.92710876464844,-290.2924499511719,-18.538837432861328,robo.r,wait=True)
                robo.move_to(61.016326904296875, -238.06103515625, 164.80154418945312,robo.r,wait=True)
                robo.move_to(258.8638916015625, -183.78578186035156, 51.27028274536133,robo.r,wait=True)
                bipar(0,robo)
                count -= 1
                continue
            if count%layout['nc'] ==0:
                x = base
                y -= h/layout['nl']
                print('caso troca de linha')
                print(f'coordenadas:{(x,y)}')
                obj = {"xaxis": x,
                   "yaxis": y,
                   "zaxis": z}
            #requests.post(base_url,json = obj)
                robo.move_to(x,y,z,robo.r,wait=True)
                count -= 1 
                continue
            x += l/layout['nc']
            print('caso normal')
            print(f'coordenadas:{(x,y)}')
            obj = {"xaxis": x,
               "yaxis": y,
               "zaxis": z}
        #requests.post(base_url,json = obj)
            robo.move_to(x,y,z,robo.r,wait=True)
            count -= 1 
    else:
        print('Layout não identificado')

if __name__ == "__main__":
    app.run()

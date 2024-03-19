# Traz a ferramenta serial para apresentar quais portas estão disponíveis
from serial.tools import list_ports
import inquirer
import pydobot
from yaspin import yaspin
import time
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.main import read_qr_code

class Robo():
    def __init__(self, continuacao: callable, robo) -> None:
        self.continuacao = continuacao
        self.robo = robo
        (self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4) = self.robo.pose()
        print(f'x:{self.x} y:{self.y} z:{self.z} j1:{self.j1} j2:{self.j2} j3:{self.j3} j4:{self.j4}')

    def origem_global(self): 
        self.robo.move_to(237, -23, 149, self.r, wait=True) 

    def origem_local(self): 
        self.robo.move_to(self.x, self.y, self.z, self.r, wait=True) 

    def move_robo_x(self, xaxis=200): #LIMITE = 360
        self.robo.move_to(self.x + xaxis, self.y, self.z, self.r, wait=True) 

    def move_robo_y(self,yaxis=100):
        self.robo.move_to(self.x, self.y + yaxis, self.z, self.r, wait=True) 

    def move_robo_z(self,zaxis=100):
        self.robo.move_to(self.x, self.y, self.z + zaxis, self.r, wait=True) 

    def move_robo_r(self, raxis=100):
        self.robo.move_to(self.x, self.y, self.z, self.r + raxis, wait=True) 

    def move_robo_location(self, xaxis, yaxis, zaxis):
        self.robo.move_to(xaxis, yaxis, zaxis, self.r, wait=True) 

    def change_speed(self, value):
        self.robo.speed(value, value)

    def close_connection(self):
        self.robo.close()
    
    def ativar_ventosa(self, resposta):
        if resposta == "a":
            self.robo.suck(True)
        if resposta == "d":
            self.robo.suck(False)

    def posicao_atual(self):
        return print(f' Posição atual: x:{self.x} y:{self.y} z:{self.z} j1:{self.j1} j2:{self.j2} j3:{self.j3} j4:{self.j4}')
    
    def pegar_medicamento(self):
        posicoes = ler_json('./posicoes.json')
        self.robo.move_to(posicoes["adeq"]["p1"]["x"], posicoes["adeq"]["p1"]["y"], posicoes["adeq"]["p1"]["z"], self.r, wait=True)
        self.robo.move_to(posicoes["adeq"]["p2"]["x"], posicoes["adeq"]["p2"]["y"], posicoes["adeq"]["p2"]["z"], self.r, wait=True)
        self.robo.suck(True)
        self.robo.move_to(posicoes["adeq"]["p3"]["x"], posicoes["adeq"]["p3"]["y"], posicoes["adeq"]["p3"]["z"], self.r, wait=True)
        self.robo.move_to(posicoes["adeq"]["p4"]["x"], posicoes["adeq"]["p4"]["y"], posicoes["adeq"]["p4"]["z"], self.r, wait=True)
        # Faz validar QrCode
        resposta = read_qr_code()
        if resposta == "em conformidade":
            print('Medicamento em conformidade')
            self.robo.move_to(posicoes["adeq"]["p5"]["x"], posicoes["adeq"]["p5"]["y"], posicoes["adeq"]["p5"]["z"], self.r, wait=True)
            self.robo.move_to(posicoes["adeq"]["p6"]["x"], posicoes["adeq"]["p6"]["y"], posicoes["adeq"]["p6"]["z"], self.r, wait=True)
            self.robo.suck(False)
        elif resposta == "vencido":
            print('Medicamento vencido')
            self.robo.move_to(posicoes["adeq"]["p5"]["x"], posicoes["adeq"]["p5"]["y"], posicoes["adeq"]["p5"]["z"], self.r, wait=True)
            self.robo.move_to(posicoes["adeq"]["p6"]["x"], posicoes["adeq"]["p6"]["y"], posicoes["adeq"]["p6"]["z"], self.r, wait=True)
            self.robo.suck(False)
        self.origem_global()

    
    def pegar_medicamento_inadequado(self):
        posicoes = ler_json('./posicoes.json')
        self.robo.move_to(posicoes["inadeq"]["p1"]["x"], posicoes["inadeq"]["p1"]["y"], posicoes["inadeq"]["p1"]["z"], self.r, wait=True)
        self.robo.move_to(posicoes["inadeq"]["p2"]["x"], posicoes["inadeq"]["p2"]["y"], posicoes["inadeq"]["p2"]["z"], self.r, wait=True)
        self.robo.suck(True)
        time.sleep(1)
        self.robo.move_to(posicoes["inadeq"]["p3"]["x"], posicoes["inadeq"]["p3"]["y"], posicoes["inadeq"]["p3"]["z"], self.r, wait=True)
        self.robo.move_to(posicoes["inadeq"]["p4"]["x"], posicoes["inadeq"]["p4"]["y"], posicoes["inadeq"]["p4"]["z"], self.r, wait=True)
        self.robo.move_to(posicoes["inadeq"]["p5"]["x"], posicoes["inadeq"]["p5"]["y"], posicoes["inadeq"]["p5"]["z"], self.r, wait=True)

def ler_json(posicoes):
    with open(posicoes, 'r') as posicoes:
        return json.load(posicoes)









# # Fecha a conexão com o robô
# robo.close()

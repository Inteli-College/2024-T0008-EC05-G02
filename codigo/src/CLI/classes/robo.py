# Traz a ferramenta serial para apresentar quais portas estão disponíveis
from serial.tools import list_ports
import inquirer
import pydobot
from yaspin import yaspin
import time


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
        self.robo.move_to(101.83129119873047, -263.7802734375, 30.708972930908203, self.r, wait=True)
        self.robo.move_to(101.83129119873047, -263.7802734375, -10.708972930908203, self.r, wait=True)
        self.robo.suck(True)
        self.robo.move_to(101.83129119873047, -263.7802734375, 120.708972930908203, self.r, wait=True)
        self.robo.move_to(219.55491638183594, -82.54214477539062, 73.68939208984375, self.r, wait=True)
        self.robo.move_to(219.55491638183594, -82.54214477539062, -30.708972930908203, self.r, wait=True)
        self.robo.suck(False)
        self.origem_global()
    
    def pegar_medicamento_inadequado(self):
        self.robo.move_to(101.83129119873047, -263.7802734375, 30.708972930908203, self.r, wait=True)
        self.robo.move_to(101.83129119873047, -263.7802734375, -19.708972930908203, self.r, wait=True)
        self.robo.suck(True)
        time.sleep(1)
        self.robo.move_to(101.83129119873047, -263.7802734375, 120.708972930908203, self.r, wait=True)
        self.robo.move_to(47.306304931640625, 210.08775329589844, 107.67615509033203, self.r, wait=True)
        self.robo.move_to(47.306304931640625, 210.08775329589844, -30.67615509033203, self.r, wait=True)









# # Fecha a conexão com o robô
# robo.close()

# robo.py

# Traz a ferramenta serial para apresentar quais portas estão disponíveis
from serial.tools import list_ports
import inquirer
import pydobot
from yaspin import yaspin
import time

# Traz o spinner para apresentar uma animação enquanto o robô está se movendo
spinner = yaspin(text="Processando...", color="yellow")

# Listas as portas seriais disponíveis
available_ports = list_ports.comports()


# Pede para o usuário escolher uma das portas disponíveis
porta_escolhida = inquirer.prompt([
    inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
])["porta"]


# Cria uma instância do robô
robo = pydobot.Dobot(port=porta_escolhida, verbose=False)

robo.speed(100, 100)

(x, y, z, r, j1, j2, j3, j4) = robo.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

def origem_global(): 
    robo.move_to(237, -23, 149, r, wait=True) 

def origem_local(): 
    robo.move_to(x, y, z, r, wait=True) 

def move_robo_x(xaxis=200): #LIMITE = 360
    robo.move_to(x + xaxis, y, z, r, wait=True) 

def move_robo_y(yaxis=100):
    robo.move_to(x, y + yaxis, z, r, wait=True) 

def move_robo_z(zaxis=100):
    robo.move_to(x, y, z + zaxis, r, wait=True) 

def move_robo_r(raxis=100):
    robo.move_to(x, y, z, r + raxis, wait=True) 

def move_robo_location(xaxis, yaxis, zaxis):
    robo.move_to(xaxis, yaxis, zaxis, r, wait=True) 

def robo_speed(value):
    robo.speed(value, value)
    
def pegar_remedio_vermelho():
    robo.suck(False)
    move_robo_location(282, 70, -4)
    robo.suck(True)
    time.sleep(5)
    move_robo_z(30)
    # origem_global()
    move_robo_location(75, -212, 30)
    robo.suck(False)


# origem_global()
pegar_remedio_vermelho()
# origem_global()

# robo.move_to_J(131.24, 212.6, 151.72, 58.31)

# Pega a posição atual do robô
posicao_atual = robo.pose()
print(f"Posição atual: {posicao_atual}")


# Fecha a conexão com o robô
robo.close()

import typer
import inquirer
from yaspin import yaspin
import time
import pydobot
from serial.tools import list_ports
from classes.config import Configurar
from classes.move import Movimentar
from classes.robo import Robo
# Cria uma instância da aplicação

app = typer.Typer()

# Estado da ferramenta
robot_tool = False

available_ports = list_ports.comports()

porta_escolhida = inquirer.prompt([inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])])["porta"]

print('Porta escolhida:', porta_escolhida)

class InteliArm(pydobot.Dobot):
    def __init__(self, port=None, verbose=False):
        super().__init__(port=port, verbose=verbose)
    
    def movej_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVJ_XYZ, wait=wait)

    def move_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVL_XYZ, wait=wait)

# Cria uma instância do robô
robo = InteliArm(port=porta_escolhida, verbose=False)
# robo = pydobot.Dobot(port=porta_escolhida, verbose=False)

(x, y, z, r, j1, j2, j3, j4) = robo.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

# Cria um  comando do CLI
@app.command()
def inicio():
    # realiza lista de perguntas para o usuário

    my_robot = Robo(continuacao=inicio, robo=robo)  # Pass both arguments to Robo
    
    perguntas = [inquirer.List("escolha", message="Deseja configurar o robô ou realizar movimentações?", choices=["configurações", "movimentações", "sair"])]
    # realiza a leitura das respostas
    respostas = inquirer.prompt(perguntas)
    match(respostas["escolha"]):
        case "configurações":
            Modo = Configurar(inicio, my_robot)
            Modo.configurar()
        case "movimentações":
            Modo = Movimentar(inicio, my_robot)
            Modo.movimentar()
        case "sair":
            robo.close()
            print('Fechando...')
    # chama a funcao que processa a operação e exibe uma spinner para o usuário
            
# Executa a aplicação
if __name__ == "__main__":
    app()
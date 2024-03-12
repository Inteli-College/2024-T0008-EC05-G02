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

robo = pydobot.Dobot(port=porta_escolhida, verbose=False)

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
# Comando para configurar pontos fixos
@app.command()
def configurar_pontos_fixos(arquivo):
    my_robot = Robo()  # Instância do robô
    config = Configurar(None, my_robot)  # Instância da classe Configurar
    config.configurar_pontos_fixos(arquivo)

# Comando para mover o robô para um ponto fixo
@app.command()
def mover_para_ponto_fixo(arquivo, nome_ponto):
    my_robot = Robo()  # Instância do robô
    mov = Movimentar(None, my_robot)  # Instância da classe Movimentar
    mov.mover_para_ponto_fixo(arquivo, nome_ponto)
            
# Executa a aplicação
if __name__ == "__main__":
    app()
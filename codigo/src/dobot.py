# robo.py

# Traz a ferramenta serial para apresentar quais portas estão disponíveis
from serial.tools import list_ports
import inquirer
import pydobot
from yaspin import yaspin

# Traz o spinner para apresentar uma animação enquanto o robô está se movendo
spinner = yaspin(text="Processando...", color="yellow")

# Listas as portas seriais disponíveis
available_ports = list_ports.comports()


# Pede para o usuário escolher uma das portas disponíveis
porta_escolhida = inquirer.prompt([
    inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
])["porta"]

# EDITAR PROMPT ABAIXO
# perguntas = inquirer.prompt([
#         inquirer.List("operacao", message="Qual operação deseja realizar?", choices=["Voltar para origem", "subtração","multiplicacao","divisao"]),
#         inquirer.Text("a", message="Digite o primeiro número"),
#         inquirer.Text("b", message="Digite o segundo número")
#     ])

# Cria uma instância do robô
robo = pydobot.Dobot(port=porta_escolhida, verbose=False)

robo.speed(300, 300)

(x, y, z, r, j1, j2, j3, j4) = robo.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

def origem_global(): 
    robo.move_to(237, -23, 149, r, wait=True) 

def origem_local(): 
    robo.move_to(x, y, z, r, wait=True) 

def move_robo(xaxis): # adicionar parametros com valor padrão
    robo.move_to(xaxis, y, z, r, wait=True) 

# robo.move_to(x + 40, y, z, r, wait=False)
# robo.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing

origem_global()


# # Inicializa o efetuador do robô
# spinner.start()
# robo.suck(True)
# # Adiciona um delay para o robô efetuar a operação
# print("atuador acionado")
# robo.wait(200)
# spinner.stop()

# # Desliga o efetuador do robô
# spinner.start()
# robo.suck(False)
# # Adiciona um delay para o robô efetuar a operação
# print("atuador desligado")
# robo.wait(200)
# spinner.stop()

# Pega a posição atual do robô
posicao_atual = robo.pose()
print(f"Posição atual: {posicao_atual}")


# Fecha a conexão com o robô
robo.close()

import time
from pydobot import Dobot

# Conecta ao Dobot Magician Lite
dobot = Dobot(port="COM4")  # Altere a porta de acordo com a configuração do seu sistema

# Função para movimentar o robô para uma posição específica
def move_to_position(x, y, z):
    dobot.move_to(x, y, z, 0, wait=True)

# Movimenta o robô para três posições diferentes
try:
    move_to_position(200, 0, 50)  # Posição 1
    time.sleep(2)  # Espera 2 segundos
    move_to_position(200, 100, 50)  # Posição 2
    time.sleep(2)  # Espera 2 segundos
    move_to_position(200, 200, 50)  # Posição 3
    time.sleep(2)  # Espera 2 segundos

except Exception as e:
    print(f"Erro: {e}")

finally:
    # Desconecta o robô
    dobot.close()

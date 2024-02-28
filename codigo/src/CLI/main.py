import typer
import inquirer
from yaspin import yaspin
import time
from classes.config import Configurar
from classes.move import Movimentar
# Cria uma instância da aplicação
app = typer.Typer()

# Estado da ferramenta
robot_tool = False

# Cria um quarto comando do CLI
@app.command()
def inicio():
    # realiza lista de perguntas para o usuário
    
    perguntas = [inquirer.List("escolha", message="Deseja configurar o robô ou realizar movimentações?", choices=["configurações", "movimentações", "sair"])]
    # realiza a leitura das respostas
    respostas = inquirer.prompt(perguntas)
    match(respostas["escolha"]):
        case "configurações":
            Modo = Configurar(inicio)
            Modo.configurar()
        case "movimentações":
            Modo = Movimentar(inicio)
            Modo.movimentar()
        case "sair":
            print('Fechando')
    # chama a funcao que processa a operação e exibe uma spinner para o usuário
# Executa a aplicação
if __name__ == "__main__":
    app()
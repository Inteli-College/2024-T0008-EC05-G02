import yaspin
import inquirer
import time
from CLI.classes.config import Configurar

class Movimentar():
    def __init__(self, continuacao: callable) -> None: 
        self.continuacao = continuacao
    def movimentos(self):
        perguntas = [inquirer.List("escolha", message="Deseja configurar o robô ou realizar movimentações?", choices=["Movimento em X", "Movimento em Y", "Movimento em Z", "Ativar/Desativar Ventosa", "Home (Retornar para posição original)"])]
        respostas = inquirer.prompt(perguntas)
        return self.processar(respostas)
    
    def processar(self, resposta):
        escolha = resposta["escolha"]
        match(escolha):
            case "Movimento em X":
                return 0
            case "Movimento em Y":
                return 0
            case "Movimento em Z":
                return 0
            case "Ativar/Desativar ventosa":
                return 0
            case "Home (Retornar para posição original)":
                return 0
            case "Retornar para"
    
    def move(self):

            
            
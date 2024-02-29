import yaspin
import inquirer
import time
from classes.robo import Robo

class Movimentar():
    def __init__(self, continuacao: callable, my_robot) -> None: 
        self.continuacao = continuacao
        self.my_robot = my_robot

    def movimentar(self):
        perguntas = [inquirer.List("escolha", message="Deseja configurar o robô ou realizar movimentações?", choices=["Movimento em X", "Movimento em Y", "Movimento em Z", "Ativar/Desativar ventosa", "Home (Retornar para posição original)", "Coordenadas da posição atual","Retornar para escolha", "Pegar medicamento"])]
        respostas = inquirer.prompt(perguntas)
        return self.processar(respostas)
    
    def processar(self, resposta):
        escolha = resposta["escolha"]
        match(escolha):
            case "Movimento em X":
                resposta = int(input("Digite o valor desejado: "))
                print(f"Valor em x escolhido: {resposta}")
                self.my_robot.move_robo_x(resposta)
                return self.continuacao()
            case "Movimento em Y":
                resposta = int(input("Digite o valor desejado: "))
                print(f"Valor em y escolhido: {resposta}")
                self.my_robot.move_robo_y(resposta)
                return self.continuacao()
            case "Movimento em Z":
                resposta = int(input("Digite o valor desejado: "))
                print(f"Valor em z escolhido: {resposta}")
                self.my_robot.move_robo_z(resposta)
                return self.continuacao()
            case "Ativar/Desativar ventosa":
                resposta = input("Digite a para ativar ou d para desativar: ")
                print(f"Valor escolhido: {resposta}")
                time.sleep(1)
                print(f"Realizando operação...")
                time.sleep(2)
                self.my_robot.ativar_ventosa(resposta)
                return self.continuacao()
            case "Home (Retornar para posição original)":
                self.my_robot.origem_global()
                return self.continuacao()
            case "Coordenadas da posição atual":
                self.my_robot.posicao_atual()
                time.sleep(2)
                return self.continuacao()
            case "Retornar para escolha":
                return self.continuacao()
            case "Pegar medicamento":
                self.my_robot.pegar_medicamento()
                return self.continuacao()
    
    def move(self):
        pass
            
            
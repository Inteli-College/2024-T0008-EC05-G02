# Importações necessárias
import inquirer
import json

class Configurar():
    def __init__(self, continuacao: callable, my_robot) -> None:
        self.continuacao = continuacao
        self.my_robot = my_robot

    def configurar(self):
        perguntas = [inquirer.List("escolha", message="Deseja Configurar qual variável?", choices=["Velocidade", "Retornar para escolha"])]
        respostas = inquirer.prompt(perguntas)
        return self.processar(respostas)
    
    def processar(self, resposta):
        escolha = resposta["escolha"]
        match(escolha):
            case "Velocidade":
                return self.definir_velocidade()
            case "Retornar para escolha":
                return self.continuacao()
        
    def definir_velocidade(self):   
        resposta = int(input("Digite a velocidade desejada: "))
        print(f"Velocidade escolhida:{resposta}")
        self.my_robot.change_speed(resposta)
        return self.continuacao()

    # Método para configurar pontos fixos
    def configurar_pontos_fixos(self, arquivo):
        pontos_fixos = self.carregar_pontos_fixos(arquivo)
        nome_ponto = input("Digite o nome do ponto fixo: ")
        x = float(input("Digite a coordenada X: "))
        y = float(input("Digite a coordenada Y: "))
        z = float(input("Digite a coordenada Z: "))
        pontos_fixos[nome_ponto] = {"x": x, "y": y, "z": z}
        self.salvar_pontos_fixos(pontos_fixos, arquivo)
        print(f"Ponto fixo '{nome_ponto}' configurado com sucesso.")

    # Método para salvar pontos fixos em arquivo JSON
    def salvar_pontos_fixos(self, pontos_fixos, arquivo):
        with open(arquivo, 'w') as f:
            json.dump(pontos_fixos, f)

    # Método para carregar pontos fixos de um arquivo JSON
    def carregar_pontos_fixos(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

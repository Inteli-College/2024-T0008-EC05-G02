import inquirer

class Configurar():
    def __init__(self, continuacao: callable) -> None:
        self.continuacao = continuacao

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
        return self.continuacao()



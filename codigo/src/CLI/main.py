import typer
import inquirer
from yaspin import yaspin
import time
from CLI.classes.config import Configurar

# Cria uma instância da aplicação
app = typer.Typer()

# Estado da ferramenta
robot_tool = False

# Cria um quarto comando do CLI
@app.command()
def inicio():
    # realiza lista de perguntas para o usuário

    perguntas = [inquirer.List("escolha", message="Deseja configurar o robô ou realizar movimentações?", choices=["configurações", "movimentações"])]
    # realiza a leitura das respostas
    respostas = inquirer.prompt(perguntas)
    # chama a funcao que processa a operação e exibe uma spinner para o usuário
    spinner = yaspin(text="Processando...", color="yellow")
    # inicia o spinner
    # spinner.start()
    # realiza a operação
    # saida = processar(respostas)
    Modo = Configurar(inicio)
    Modo.configurar()
    # para o spinner
    # spinner.stop()
    # exibe o resultado
    # print(saida)
    # continuar = typer.confirm("Deseja continuar?")
    # if continuar == True:
    #     movimentos()

# def verificar(dados):
#     print(dados)
#     operacao = dados["operacao"]
#     if operacao == "ativar ou desativar ventosa":
#         return inquirer.Text("a", message="Digite (a) para ativar ou (d) para desativar")
#     else:
#         return inquirer.Text("a", message="Digite o valor da posição")
        
# Função que processa a operação
# def processar(dados):
#     print(dados)
#     time.sleep(1)
#     operacao = dados["escolha"]
#     dados = inquirer.prompt([verificar(dados)])
#     a = dados["a"]
#     if operacao == "movimento em x":
#         return (a)
#     elif operacao == "movimnto em y":
#         return (a)
#     elif operacao == "movimento em z":
#         return (a)
#     elif operacao == "ativar ou desativar ventosa":
#         return (a)
    
# Executa a aplicação
if __name__ == "__main__":
    app()
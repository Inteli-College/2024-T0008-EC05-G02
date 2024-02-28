import typer
import inquirer
from yaspin import yaspin
import time

# Cria uma instância da aplicação
app = typer.Typer()

# Estado da ferramenta
robot_tool = False

# Cria um quarto comando do CLI
@app.command()
def movimentos():
    # realiza lista de perguntas para o usuário
    perguntas = [
        inquirer.List("operacao", message="Qual movimento deseja realizar?", choices=["movimento em x", "movimento em y","movimento em z","ativar ou desativar ventosa"])
    ]	
    # realiza a leitura das respostas
    respostas = inquirer.prompt(perguntas)
    # chama a funcao que processa a operação e exibe uma spinner para o usuário
    spinner = yaspin(text="Processando...", color="yellow")
    # inicia o spinner
    # spinner.start()
    # realiza a operação
    saida = processar(respostas)
    # para o spinner
    # spinner.stop()
    # exibe o resultado
    print(saida)
    continuar = typer.confirm("Deseja continuar?")
    if continuar == True:
        movimentos()

def verificar(dados):
    print(dados)
    operacao = dados["operacao"]
    if operacao == "ativar ou desativar ventosa":
        return inquirer.Text("a", message="Digite (a) para ativar ou (d) para desativar")
    else:
        return inquirer.Text("a", message="Digite o valor da posição")
        
# Função que processa a operação
def processar(dados):
    print(dados)
    time.sleep(1)
    operacao = dados["operacao"]
    dados = inquirer.prompt([verificar(dados)])
    a = dados["a"]
    if operacao == "movimento em x":
        return (a)
    elif operacao == "movimnto em y":
        return (a)
    elif operacao == "movimento em z":
        return (a)
    elif operacao == "ativar ou desativar ventosa":
        return (a)
    match(operacao):
        case "movimento em x":
            return (a)
        case "movimnto em y":
            return (a)
        case "movimento em z":
            return (a)
    
# Executa a aplicação
if __name__ == "__main__":
    app()
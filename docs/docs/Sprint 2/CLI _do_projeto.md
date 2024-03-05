---
sidebar_position: 3
title: "CLI do projeto"
---

# CLI do Projeto


Nessa seção, é possível acompanhar a documentação da CLI (Comnad Line Interface) do projeto e como seu código está organizado e interligado com o funcionamento do robô.


## O que é CLI

A CLI, ou Interface de Linha de Comando, é uma forma de interação com sistemas de computador ou dispositivos através de comandos de texto. Diferente das interfaces gráficas, que utilizam elementos visuais como ícones e menus, a CLI requer que o usuário digite comandos específicos para executar tarefas.

Geralmente, é utilizada por desenvolvedores e administradores de sistemas, ou em situações onde a interface gráfica não está disponível ou não é apropriada.
## O CLI atual

Ao iniciar a interface por linha de comando, o usuário é apresentado ao menu principal de escolhas, oferecendo as opções de configurações, movimentações e sair.

Ao selecionar configurações, a interface é redirecionada para a central de configurações, onde o usuário pode ajustar a velocidade do robô conforme suas necessidades.

Por outro lado, ao optar por movimentações, a interface é direcionada para outra central de escolhas, onde o usuário pode selecionar o tipo de movimento que deseja realizar. As opções disponíveis são:

- Movimento em X
- Movimento em Y
- Movimento em Z
- Ativar/Desativar ventosa
- Home (Retornar para posição original)
- Coordenadas da posição atual
- Retornar para escolha
- Pegar medicamento
- Pegar medicamento inadequado

Cada uma dessas opções desencadeia uma ação específica no robô, cujos detalhes serão explicados a seguir. Caso desejado, é possível acompanhar os vídeos das funcionalidades [aqui](https://drive.google.com/drive/folders/1buMb9bnXaBRkJwJceaT4ler247zevyVJ?usp=sharing).

### Movimento em X, Y e Z

Ao escolher essa opção, o usuário é solicitado a inserir a quantidade de movimento desejada para o robô em cada um dos eixos X, Y e Z. Após a confirmação, o robô executa o movimento e é redirecionado para a distância indicada.

### Ativar/Desativar ventosa

Ao selecionar essa opção, o usuário é solicitado a inserir "a" para ativar ou "d" para desativar a ventosa conectada ao robô. Isso permite que o robô pegue ou solte objetos em contato com a ventosa.

### Home

Essa opção faz com que o robô retorne à sua posição original pré-definida.

### Coordenadas da posição atual

Ao escolher essa opção, o usuário recebe as coordenadas da posição atual do robô.

### Pegar medicamento

Essa opção ativa a funcionalidade do robô para pegar medicamentos em conformidade, de acordo com uma movimentação pré-definida.

### Pegar medicamento inadequado

Essa opção ativa a funcionalidade do robô para pegar medicamentos inadequados, de acordo com uma movimentação pré-definida.

## Estrutura do código

O código relacionado à CLI, localizado na pasta de mesmo nome, é estruturado com uma pasta chamada "classes", um arquivo python "main.py" e outro arquivo json "posicoes.json". A seguir, é apresentada uma estrutura mais detalhada:

### Classes

Na pasta "Classes", existem três arquivos python: "config.py", "move.py" e "robo.py", cada um responsável por realizar funcionalidades específicas que serão chamadas pelo main ao executar o código.

#### config.py

Neste arquivo python, existe uma classe chamada `Configurar()`. Esta classe contém três funções principais:

- `configurar()`: utilizando o Inquirer, essa função é responsável por listar opções no terminal assim que o código é acionado. Quando o usuário escolhe uma opção, a resposta é registrada e utilizada pela função `processar()`.
- `processar()`: essa função tem como objetivo, utilizando a escolha feita pelo usuário anteriormente, realizar alguma funcionalidade pré-programada. Caso o usuário escolha "velocidade", a funcionalidade executa a função `definir_velocidade()`. Caso ele escolha "retornar para escolha", é executada a função `continuacao()`, não declarada dentro desse arquivo.
- `definir_velocidade()`: essa função é responsável por acionar uma pergunta para o usuário de qual é o valor desejado para a velocidade. Ao responder, essa velocidade é atualizada para o robô.

#### move.py

Neste arquivo python, existe uma classe chamada `Movimentar()`. Esta classe contém duas funções principais:

- `movimentar()`: utilizando o Inquirer, essa função é responsável por listar opções no terminal assim que o código é acionado. Quando o usuário escolhe uma opção, a resposta é registrada e utilizada pela função `processar()`.
- `processar()`: essa função tem como objetivo, utilizando a escolha feita pelo usuário anteriormente, realizar alguma funcionalidade pré-programada. Existem no total 9 possibilidades de escolha e, ao dar "enter", é retornada uma função de ação para o robô.

#### robo.py

Neste arquivo python, existe uma classe chamada `Robo()`. Esta classe contém várias funções interligadas à biblioteca Pydobot que realizam ações de forma direta no robô. As funções principais que fazem parte da CLI dessa Sprint são:

- `origem_robo()`: retorna o robô para uma posição pré-definida central.
- `move_robo_x()`: movimenta o robô pelo eixo x de acordo com uma posição especificada.
- `move_robo_y()`: movimenta o robô pelo eixo y de acordo com uma posição especificada.
- `move_robo_z()`: movimenta o robô pelo eixo z de acordo com uma posição especificada.
- `change_speed()`: altera a velocidade de movimentação do robô.
- `ativar_ventosa()`: ativa ou desativa a ventosa do robô.
- `posicao_atual()`: retorna a posição atual do robô no terminal.
- `pegar_medicamento()`: movimenta o robô por um fluxo de posições pré-definidas em um arquivo json.
- `pegar_medicamento_inadequado()`: movimenta o robô por um segundo fluxo de posições pré-definidas em um arquivo json.
- `close_connection()`: fecha a conexão do robô na porta serial.

Além da classe, existe uma outra função `ler_json()`, que permite a comunicação com as posições em json.

### main.py

O arquivo main.py contém o código central que inicia a comunicação do robô com a porta serial, cria uma instância convocando as funcionalidades do Pydobot e roda a função `inicio()`. Esta função retorna uma lista com as opções "configuração", "movimentação" e "sair", sendo que no primeiro e segundo caso tornam suas respectivas classes e, no terceiro caso, fecha a conexão com o robô.

### posicoes.json

Neste arquivo json, são registradas as posições que serão utilizadas para movimentar o robô em um fluxo específico. O arquivo é dividido pelo tipo de fluxo, as diferentes posições, e as coordenadas x, y e z.








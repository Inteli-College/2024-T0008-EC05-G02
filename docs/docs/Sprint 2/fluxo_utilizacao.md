---
sidebar_label: 'Fluxo de Utilização da Solução'
sidebar_position: 1
---

#  Fluxo de usuário

O mapa de fluxo de usuário foi criado para facilitar a compreensão do funcionamento da solução web, da jornada e comportamento do usuário, mostrando as possíveis telas que o usuário pode acessar e as situações que podem ocorrer durante o uso da solução. O mapa foi dividido em três partes, cada uma representando uma etapa do fluxo de uso da solução web.

## 1. Início

Na primeira parte do fluxo o auxiliar de emergência, após o posicionamento do robô automatizado e do carrinho que dispõe dos medicamentos, utilizará o notebook disponível no momento para abrir a tela inicial da solução web. Nela, há quatro opções disponíveis através de botões: `Abastecimento`, `Reabastecimento`, `Manual` e `Histórico de relatórios`, cada uma com sua respectiva tela de destino.

![Flow parte 1](../../static/img/FlowParte1.drawio.png)

## 2. (Re)Abastecimento/Situação dos medicamentos

Na segunda parte do fluxo, são fornecidos informações dos medicamentos do carrinho durante o processo do abastecimento do carrinho, iniciado através do botão de "Iniciar bipagem", sendo que estes podem se encontrar nas seguintes situações: `Em conformidade`, `Próximo à validade` `Dosagem errada` e `Código inválido`. Cada uma dessas situações possui uma tela de destino, que apresenta as informações necessárias para o usuário tomar a decisão correta do medicamento em questão.

![Flow parte 2](../../static/img/FlowParte2.drawio.png)

## 3. Processo de bipagem

Na terceira e última parte do fluxo, inicia-se o processo de bipagem dos medicamentos recém posicionados do carrinho. Neste mapa são apresentados as possíveis situações após o processo de bipagem, caso o processo seja de abastecimento ou reabastecimento, caso haja itens faltantes e como a visualização do histórico de relatórios.

![Flow parte 3](../../static/img/FlowParte3.drawio.png)
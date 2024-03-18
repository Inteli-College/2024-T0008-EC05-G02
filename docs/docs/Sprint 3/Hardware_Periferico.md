---
sidebar_position: 1
title: "Hardware Periférico"
---

# Hardware Periférico

Ao longo da Sprint 3, o foco foi no hardware periférico da nossa solução. Tendo em vista que o nosso propósito é tornar o processo mais rastreável e seguro, adicionamos sensores e câmeras a um circuito com microcontrolador integrado ao sistema do robô.

Os tópicos abaixo foram divididos em: diagrama do hardware periférico, sensor infravermelho, câmera com reconhecimento de QR Codes e integração com o robô.

## Diagrama do hardware periférico

![Diagrama do Hardware Periférico](../../static/img/diagrama_periferico.png)

O diagrama do hardware periférico acima destaca o sensor infravermelho que está conectado a um microcontrolador e este, por sua vez, conectado a um buzzer. 

Materiais que foram necessários: 
* Raspberry Pi Pico W - microcontrolador RP2040 no diagrama;
* Módulo sensor infravermelho TCRT5000 - como ITR9608-F no diagrama;
* Buzzer;
* Protoboard;
* Fios de conexão (jumpers).

Para a montagem do circuito:
1. Alimentação do Módulo TCRT5000:
* VCC para 3.3V: Pino VCC do TCRT5000 conectado a um pino de 3.3V do Pico W;
* GND para GND: A conexão terra (GND) do lado negativo do infravermelho ao GND do Pico W. E o lado do emissor do fototransistor, que também precisa ser conectado ao terra (GND).

2. Saída do Módulo TCRT5000:
* Saída Analógica (AO): conectada ao pino GP26.

3. Conexão do Buzzer:
* Buzzer ao GP15: Um dos pinos do buzzer conectado ao GP15;
* Buzzer ao GND: E o outro pino ao GND.

Link para download dos arquivos [aqui](https://drive.google.com/drive/folders/1KePuMLv8DWsRA4y9oFspp2WJk1aRgLx7?usp=sharing). 

## Sensor infravermelho

![Sensor infravermelho](../../static/img/sensor_infravermelho.jpeg)

Esta foto representa o circuito do sensor infravermelho comentado no diagrama do tópico anterior. Ele serve para detectarmos se o robô pegou ou não um medicamento. Ele foi posicionado dentro do robô de forma que consiga detectar se há algum objeto na sua frente. Quando há um medicamento preso pela ventosa, ele solta um apito intervalado pelo buzzer. Quando não há medicamento, ele para de apitar, indicando que há algo errado e que não foi possível pegar o medicamento. 

Esta etapa serve para garantirmos mais segurança na operação.

## Câmera com reconhecimento de QR Codes

A câmera foi integrada ao sistema do robô para que ele consiga identificar os medicamentos que serão bipados, auxiliando tanto no registro da montagem de novos carrinhos quanto no reabastcimento, com a verificação de quais medicamentos permanecem no carrinho. Essa etapa é fundamental para garantir a rastreabilidade e segurança do processo, evitando a troca de medicamentos e garantindo que os medicamentos estejam dentro do prazo de validade e com a dosagem correta. 

 Em relação ao posicionamento da câmera, ela foi fixada entre a bandeja de itens a serem veficados e a bandeja dos itens já verificados, como mostra a imagem abaixo.

![Câmera com reconhecimento de QR Codes](../../static/img/camera_qrcode.jpg)

Dessa forma, a movimentação do robô é facilitada por estar entre as bandejas e, como já está no meio do caminho percorrido pelo robô, o processo de bipagem se torna otimizado.

Para a integração da câmera, foi necessário instalar as bibliotecas `opencv`, usada no tratamento da visão computacional, e `qreader`, responsável por decodificar os QR Codes. A grande vantagem do `qreader ` se dá pela sua habilidade em captar os códigos até mesmo em ângulos não tão favorecidos devido ao seu modelo de treinamento amplo e variado, permitindo a identificação de QR Codes em diversas imagens e situações. 

Apesar do potencial do `qreader`, a verificação por meio da câmera ainda está em fase de testes para garantir a eficiência do reconhecimento dos QR Codes. No momento atual de desenvolvimento, a câmera é acionada e assim que o QR code é identificado, a câmera captura uma foto, salva no arquivo local e exibe as informações decodificadas no terminal, além de trazer uma validação se o medicamento está em conformidade, vencido ou com a dosagem errada.

Portanto, é esperado que esse processo seja aprimorado para que a câmera consiga identificar os QR Codes de forma mais rápida e eficiente, garantindo a segurança e rastreabilidade do processo.

## Integração com o robô

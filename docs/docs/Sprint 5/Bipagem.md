---
sidebar_label: 'Bipagem: mostrando os remédios'
sidebar_position: 1
---

# Contexto

A bipagem de remédios em tempo real é essencial para garantir a precisão e eficiência no processo de administração de medicações. Utilizando um robô equipado com uma câmera e conectado via WebSocket, este sistema permite a verificação e confirmação visual dos remédios antes da sua administração, aumentando a segurança do paciente e minimizando erros.

# Robô + Websocket

## O Sistema

O coração deste sistema é um conjunto de três componentes principais: o **robô**, a **câmera** e o **WebSocket**. O robô, operando em conjunto com a câmera, é responsável por identificar os remédios através da leitura de códigos QR. Após a leitura, os dados são transmitidos em tempo real através de uma conexão WebSocket, garantindo que as informações mais atualizadas estejam sempre disponíveis.

### Funcionamento

1. **Robô**: Equipado com uma câmera, o robô realiza a bipagem dos remédios lendo os códigos QR impressos nas embalagens.
2. **Câmera**: Capta as imagens dos códigos QR, que são então processadas para extrair as informações dos remédios.
3. **WebSocket**: Facilita a comunicação em tempo real entre o backend e o frontend, transmitindo os dados dos remédios lidos pela câmera.

## Implementação

- **`QrCodeWrapper`**: Este wrapper gerencia a leitura de códigos QR e a comunicação com o WebSocket para enviar os dados capturados.
- **`RobotWrapper`**: Gerencia as ações do robô, incluindo a bipagem de layouts de medicamentos.
- **`WebSocketWrapper`**: Encarrega-se de estabelecer a conexão WebSocket e gerenciar a transmissão de mensagens entre o backend e o frontend.

# Interface

## Recepção de Dados

O frontend recebe os dados dos remédios através da conexão WebSocket, onde as informações atualizadas sobre cada remédio são exibidas em tempo real. Este processo assegura que os operadores tenham acesso imediato às informações necessárias para validar a precisão dos remédios bipados pelo robô.

### Fluxo de Dados

1. **Leitura do QR Code**: Quando um remédio é bipado, a câmera lê o QR Code e os dados são processados.
2. **Transmissão WebSocket**: Os dados são enviados ao frontend através do WebSocket.
3. **Visualização**: O frontend atualiza a interface com as informações recebidas, permitindo a verificação visual dos remédios.

Este sistema integrado não apenas otimiza o processo de administração de medicamentos mas também introduz um novo nível de segurança e eficiência, essencial para ambientes de cuidados de saúde.

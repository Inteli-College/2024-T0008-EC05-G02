import React, { useEffect, useState } from "react";
import './styleConformidade.css';
import DrugCard from '../../components/drugCard';
import remedio from './Norepinefrina.jpg';

export default function WebSocketClientComponent() {
    const [latestMessage, setLatestMessage] = useState("");
    const webSocketRef = React.useRef(null);

    useEffect(() => {
        webSocketRef.current = new WebSocket("ws://127.0.0.1:5000");

        const ws = webSocketRef.current;

        ws.onopen = () => {
            console.log("Connected to WebSocket server.");
            const messageJson = JSON.stringify({ "target": "QrCode", "action": "read_qr_code" });
            ws.send(messageJson);
        };

        ws.onmessage = (event) => {
            console.log('Message from server ', event.data);
            const messageObj = JSON.parse(event.data);
            setLatestMessage(messageObj);
        };

        ws.onclose = () => {
            console.log("Disconnected from WebSocket server.");
        };

        ws.onerror = (err) => {
            console.error('WebSocket encountered error: ', err.message, 'Closing socket');
            ws.close();
        };

        return () => {
            if(ws.readyState === WebSocket.OPEN) {
                ws.close();

            }
        };
    }, []);

    function renderDrugCard(message) {
      switch (message[0]) {
        case "Medicamento incorreto":
          return (
            <DrugCard
              color="red"
              status="Incorreto"
              image={remedio}
              name={message[1][0]}
              dose={message[1][1]}
              expiration={message[1][2]}
              batch={message[1][3]}
              supplier={message[1][1]}
            />
          );
    
        case "Medicamento correto, mas expirado":
          return (
            <DrugCard
              color="yellow"
              status="Expirado"
              image={remedio}
              name={message[1][0]}
              dose={message[1][1]}
              expiration={message[1][2]}
              batch={message[1][3]}
              supplier={message[1][1]}
            />
          );
    
        case "Medicamento correto, mas próximo da data de validade":
          return (
            <DrugCard
              color="red"
              status="Próximo da validade"
              image={remedio}
              name={message[1][0]}
              dose={message[1][1]}
              expiration={message[1][2]}
              batch={message[1][3]}
              supplier={message[1][1]}
            />
          );
    
        case "Medicamento correto e válido":
          return (
            <DrugCard
              color="green"
              status="Correto e válido"
              image={remedio}
              name={message[1][0]}
              dose={message[1][1]}
              expiration={message[1][2]}
              batch={message[1][3]}
              supplier={message[1][1]}
            />
          );

        case "Dosagem incorreta":
          return (
            <DrugCard
              color="red"
              status="Inválido. Dosagem incorreta."
              image={remedio}
              name={message[1][0]}
              dose={message[1][1]}
              expiration={message[1][2]}
              batch={message[1][3]}
              supplier={message[1][1]}
            />
          );
    
        default:
          return <p>Unknown status</p>;
      }
    }

    return (
        <div className="messages">
            {latestMessage && <>
            {/* <p>{latestMessage.data}</p> */}
            {renderDrugCard(latestMessage.data)}
            </>} {/* Mostra a última mensagem */}
        </div>
    );
}

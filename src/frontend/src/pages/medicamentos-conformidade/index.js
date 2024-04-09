import React, { useEffect, useState } from "react";
import './styleConformidade.css';
import DrugCard from '../../components/drugCard';
import remedio from './Norepinefrina.jpg';

export default function WebSocketClientComponent() {
    const [latestMessage, setLatestMessage] = useState("");
    const webSocketRef = React.useRef(null);

    useEffect(() => {
        webSocketRef.current = new WebSocket("ws://127.0.0.1:3000/ws");

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
      switch (message) {
        case "Medicamento incorreto":
          return (
            <DrugCard
              color="red"
              status="Incorreto"
              image={remedio}
              name="Incorrect Drug"
              dose="N/A"
              expiration="N/A"
              batch="N/A"
              supplier="N/A"
            />
          );
    
        case "Medicamento correto, mas expirado":
          return (
            <DrugCard
              color="yellow"
              status="Expirado"
              image={remedio}
              name="Correct Drug"
              dose="5mg"
              expiration="Expired Date"
              batch="B2022"
              supplier="OldPharma"
            />
          );
    
        case "Medicamento correto, mas próximo da data de validade":
          return (
            <DrugCard
              color="yellow"
              status="Próximo da Validade"
              image={remedio}
              name="Correct Drug"
              dose="5mg"
              expiration="Near Expiry Date"
              batch="C2023"
              supplier="CurrentPharma"
            />
          );
    
        case "Medicamento correto e válido":
          return (
            <DrugCard
              color="green"
              status="Válido"
              image={remedio}
              name="Correct Drug"
              dose="5mg"
              expiration="Valid Date"
              batch="A2024"
              supplier="NewPharma"
            />
          );
    
        default:
          return <p>Unknown status</p>;
      }
    }

    return (
        <div className="messages">
            {latestMessage && <>
            <p>{latestMessage.data}</p>
            {renderDrugCard(latestMessage.data)}
            </>} {/* Mostra a última mensagem */}
        </div>
    );
}

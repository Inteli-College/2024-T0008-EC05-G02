import React from 'react';
import './style.css'; // Importa o arquivo CSS
import StyledButton from '../../components/styledButton';

const handleVerificarBandeja = () => {
    console.log("Aqui está a bandeja")
  };
  
const handleIniciarBipagem = () => {
    console.log("Clicado...")
  };
  

function ReposicaoItens() {
  return (
    <div className="divContainer">
      <h1 className="paragraphText">Abastecimento</h1>
      <div className="infoContainer">
        <p className="infoTextGradient">2ª Etapa - Reposição de itens</p>
      </div>
      <div className="infoButtonContainer">
        <StyledButton route="/" text="Verificar bandeja" colorbutton="yellow" onClick={handleVerificarBandeja}></StyledButton>
        <StyledButton route="/segunda-bipagem-finalizada" text="Iniciar bipagem" colorbutton="gray" onClick={handleIniciarBipagem}></StyledButton>
      </div>
    </div>
  );
}

export default ReposicaoItens;
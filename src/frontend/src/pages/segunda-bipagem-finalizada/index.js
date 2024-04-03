import React from 'react';
import './style.css'; // Importa o arquivo CSS
import StyledButton from '../../components/styledButton';


const handleRelatorioCompleto = () => {
  console.log("Aqui está o relatório completo!")
};

const handleReabastcerFaltantes = () => {
  console.log("Clicado...")
};

function SegundaBipagemFinalizada() {
  return (
    <div className="divContainer">
      <h1 className="paragraphText">2ª Bipagem finalizada!</h1>
      <div className="infoContainer">
        <p className="infoTextGradient">Parabéns! Todos os medicamentos foram repostos.</p>
      </div>
      <div className="infoButtonContainer">
        <StyledButton route="/historico" text="Ver relatório completo" colorbutton="blue" onClick={handleRelatorioCompleto}></StyledButton>
        <StyledButton route="/" text="Finalizar processo" colorbutton="green" onClick={handleReabastcerFaltantes}></StyledButton>
      </div>
    </div>
  );
}

export default SegundaBipagemFinalizada;
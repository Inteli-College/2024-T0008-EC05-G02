import React from 'react';
import { Button } from 'antd';
import './Norepinefrina.jpg';
import './style.css';
import remedio from './Norepinefrina.jpg';


function MedicamentoConformidade() {
  return (

<>
    <h1 className="title">Em Criação...</h1>
    
    <div className="card-container">  
      <div className="card-header">
        <h2 className="subtitle">Em conformidade</h2>
      </div>
      <div className="card-content">
            <img
            alt="Imagem do produto"
            className="product-image"
            src={remedio} 
            />
            <div className="product-details">
                <p className="product-name">Nome: Norepinefrina</p>
                <p><span className="product-detail-label">Nome:</span> Norepinefrina</p>
                <p><span className="product-detail-label">Dosagem:</span> 4mg/4ml</p>
                <p><span className="product-detail-label">Data de validade:</span> 09/10/2024</p>
                <p><span className="product-detail-label">Lote:</span> A20230910F3</p>
                <p><span className="product-detail-label">Fornecedor:</span> Novafarma</p>
            </div>
        </div>
    </div>

    <div className="card-footer">
        <Button type="primary" className="pause-button">Pausar Bipagem</Button>
        <Button type="danger" className="finish-button">Finalizar Bipagem</Button>
      </div>

 </>
  );
}

export default MedicamentoConformidade;

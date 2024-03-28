import React from 'react';
import './style.css'; // Importa o arquivo CSS
import { Table } from "antd";
import StyledButton from '../../components/styledButton';

const dataSource = [
  {
    key: '1',
    medicamento: 'Gluconato de Cálcio',
    dosagem: '20mg',
    quantidade: 4,
  },
  {
    key: '2',
    medicamento: 'Prometazina',
    dosagem: '20mg',
    quantidade: 1,
  },
  {
    key: '3',
    medicamento: 'Dobutamina + Glicose 50%',
    dosagem: '500mg',
    quantidade: 2,
  },
  {
    key: '4',
    medicamento: 'Diazepam + Suxametanio',
    dosagem: '10mg',
    quantidade: 3,
  },
  {
    key: '5',
    medicamento: 'Dopamina',
    dosagem: '1mg',
    quantidade: 1,
  },
  {
    key: '6',
    medicamento: 'Succinil + Naloxona',
    dosagem: '500mg',
    quantidade: 2,
  },
];

const columns = [
  {
    title: 'Medicamento',
    dataIndex: 'medicamento',
    key: 'medicamento',
  },
  {
    title: 'Dosagem',
    dataIndex: 'dosagem',
    key: 'dosagem',
  },
  {
    title: 'Quantidade faltante',
    dataIndex: 'quantidade',
    key: 'quantidade',
  },
];


const handleRelatorioCompleto = () => {
  console.log("Aqui está o relatório completo!")
};

const handleReabastcerFaltantes = () => {
  console.log("Reabastecendo...")
};

function BipagemFinalizada() {
  return (
    <div className="divContainer">
      <h1 className="paragraphText">Bipagem finalizada!</h1>
      <p className="paragraphText">A partir dos medicamentos identificados, foram encontradas irregularidades:</p>
      <div className="infoContainer">
        <p className="infoTextRed">Medicamentos vencidos: 25</p>
        <p className="infoTextYellow">Medicamentos com dosagem errada: 2</p>
      </div>
      <p className="paragraphText">Os seguintes não foram encontrados durante a separação: </p>
      <Table dataSource={dataSource} columns={columns} pagination={{ pageSize: 3 }}/>
      <div className="infoButtonContainer">
        <StyledButton text="Ver relatório completo" colorbutton="blue" onClick={handleRelatorioCompleto}></StyledButton>
        <StyledButton route="/em-conformidade" text="Reabastecer itens faltantes" colorbutton="green" onClick={handleReabastcerFaltantes}></StyledButton>
      </div>
    </div>
  );
}

export default BipagemFinalizada;
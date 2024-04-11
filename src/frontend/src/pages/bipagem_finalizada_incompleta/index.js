import React, { useEffect, useState} from 'react';
import './bipagem_incompleta.css';
import { Table } from "antd";
import StyledButton from '../../components/styledButton';
import Axios from 'axios';
import { useParams } from 'react-router-dom';

const columns = [
  {
    title: 'Medicamento',
    dataIndex: 'nome',
    key: 'nome',
  },
  {
    title: 'Dose',
    dataIndex: 'dose',
    key: 'dose',
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

function BipagemIncompletaFinalizada() {
  let id_operacao= useParams();	
  const [dataSource, setDataSource] = useState([]);
  const [vencidos, setVencidos] = useState(0);
  const [doseErrada, setDoseErrada] = useState(0);

  useEffect(() => {
    const getItensFaltantes = async () => {
    try{
      const response = await Axios.get(`http://localhost:8000/fim-bipagem/${id_operacao.id_operacao}`);
      var dados = response.data
      console.log(response.data)
      setDataSource([...dados[0]]);
      setVencidos(dados[1]);
      setDoseErrada(dados[2]);

    }catch (error){
        console.error("There was an error fetching the data:", error);
      };
    }
    getItensFaltantes();
    console.log(dataSource);
    console.log(vencidos);
    console.log(doseErrada);
  }, [id_operacao]);


  return (
    <div className="divContainerB">
      <h1 className="paragraphTextB">Bipagem finalizada!</h1>
      <p className="paragraphTextB">A partir dos medicamentos identificados, foram encontradas irregularidades:</p>
      <div className="infoContainerB">
        <p className="infoTextRedB">Medicamentos vencidos: {vencidos}</p>
        <p className="infoTextYellowB">Medicamentos com dosagem errada: {doseErrada}</p>
      </div>
      <p className="paragraphTextB">Os seguintes não foram encontrados durante a separação: </p>
      <Table dataSource={dataSource} columns={columns} pagination={{ pageSize: 3 }}/>
      <div className="infoContainerB">
        <StyledButton route="/relatorio/13" text="Ver relatório completo" colorbutton="blue" onClick={handleRelatorioCompleto}></StyledButton>
        {/* <StyledButton route="/em-conformidade" text="Reabastecer itens faltantes" colorbutton="green" onClick={handleReabastcerFaltantes}></StyledButton> */}
        <StyledButton route="/" text="Voltar para o início" colorbutton="green"></StyledButton>
      </div>
    </div>
  );
}

export default BipagemIncompletaFinalizada;
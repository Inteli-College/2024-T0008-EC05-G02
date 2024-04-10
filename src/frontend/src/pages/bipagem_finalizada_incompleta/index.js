import React, { useEffect, useState} from 'react';
import './bipagem_incompleta.css';
import { Table } from "antd";
import StyledButton from '../../components/styledButton';
import Axios from 'axios';

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
    title: 'Data de validade',
    dataIndex: 'validade',
    key: 'validade',
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

  useEffect(() => {
    Axios.get(`http://localhost:8000/bipagem/${id_operacao.id_operacao}`),
      .then(response => {
        var colunas = response.data
        console.log(response.data)

        setDataSource(colunas);
      })
      .catch(error => {
        console.error("There was an error fetching the data:", error);
      });

  }, []);

  useEffect(() => {
    const getItensFaltantes = async () => {
        console.log(id_operacao);
        try {
            const [response1, response2] = await Promise.all([
                Axios.get(`http://localhost:8000/bipagem/${id_operacao.id_operacao}`),
                Axios.get(`http://localhost:8000/operacao/${id_operacao.id_operacao}`)
            ]);
            
            console.log(response1.data);
            console.log(response2.data);
    const medicamentos = response1.data;
            const operacao = response2.data;
    const medicamentos_agrupados = medicamentos.reduce((acc, curr) => {
      if (acc[curr.nome]) {
        acc[curr.nome].count += 1;
      } else {
        acc[curr.nome] = { ...curr, count: 1 };
      }
      return acc;
    }, {});
            setOperacao(operacao);
    setRelatorio(Object.values(medicamentos_agrupados));
    
        } catch (error) {
            console.error(error);
        }
    };

    getItensFaltantes();
}, [id_operacao]);

  return (
    <div className="divContainerB">
      <h1 className="paragraphTextB">Bipagem finalizada!</h1>
      <p className="paragraphTextB">A partir dos medicamentos identificados, foram encontradas irregularidades:</p>
      <div className="infoContainerB">
        <p className="infoTextRedB">Medicamentos vencidos: 1</p>
        <p className="infoTextYellowB">Medicamentos com dosagem errada: 2</p>
      </div>
      <p className="paragraphTextB">Os seguintes não foram encontrados durante a separação: </p>
      <Table dataSource={dataSource} columns={columns} pagination={{ pageSize: 3 }}/>
      <div className="infoButtonContainerB">
        <StyledButton text="Ver relatório completo" colorbutton="blue" onClick={handleRelatorioCompleto}></StyledButton>
        <StyledButton route="/em-conformidade" text="Reabastecer itens faltantes" colorbutton="green" onClick={handleReabastcerFaltantes}></StyledButton>
      </div>
    </div>
  );
}

export default BipagemIncompletaFinalizada;
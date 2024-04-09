import {React, useEffect, useState} from 'react';
import { Button } from 'antd';
import './Norepinefrina.jpg';
import './style.css';
import remedio from './Norepinefrina.jpg';
import DrugCard from '../../components/drugCard';
import { useNavigate } from 'react-router-dom';
import Axios from 'axios';


function MedicamentoConformidade() {
  const navigate = useNavigate();
  const [informacao_med, setInformacao_med] = useState({});

  // Get do endpoint

  useEffect(() => { 
    const getMedicamento = async () => {
      try {
        const response = await Axios.get('http://localhost:5000/qreader/');
        console.log(response.data);
        setInformacao_med(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    getMedicamento();
  }, []);

  return (
    <div className="conformidade">
    <h1 className="page-title">Em Criaçãoooooo...</h1>
        <DrugCard 
        color={informacao_med.status === "Em conformidade" ? "green" : "red"}
        status= {informacao_med.status }
        image={remedio} 
        name={informacao_med.nome}
        dose={informacao_med.dose}
        expiration={informacao_med.validade}
        batch={informacao_med.lote}
        supplier={informacao_med.fornecedor}
        />
    {/* </div> */}
    <div className="card-footer">
        <Button type="primary" className="pause-button">Pausar Bipagem</Button>
        <Button type="danger" className="finish-button" onClick={()=> navigate("/fim-bipagem")}>Finalizar Bipagem</Button>
      </div>
 </div>
  );
}

export default MedicamentoConformidade;

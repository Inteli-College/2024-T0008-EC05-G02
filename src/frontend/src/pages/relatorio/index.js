import { useEffect, useState } from 'react';
import Axios from 'axios';
import { Table } from 'antd';
import { useNavigate } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import './relatorio.css';
import { Link } from 'react-router-dom';
import StyledButton from '../../components/styledButton';

function Relatorio() {
	let id_operacao= useParams();	
    const navigate = useNavigate();
    const [relatorio, setRelatorio] = useState([]);
    const [operacao, setOperacao] = useState([]);

    useEffect(() => {
        const getRelatorio = async () => {
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

        getRelatorio();
    }, [id_operacao]);

    const columns = [
        {
            title: 'Nome',
            dataIndex: 'nome',
            key: 'nome',
            width: "10%",
            align: "center",
        },
        {
            title: 'Dose',
            dataIndex: 'dose',
            key: 'dose',
            width: "15%",
            align: "center"
        },
        {
            title: 'Validade',
            dataIndex: 'validade',
            key: 'validade',
            width: "10%",
            align: "center",
        },
        {
            title: 'Lote',
            dataIndex: 'lote',
            key: 'lote',
            width: "15%",
            align: "center",
        },
        {
            title: 'Fornecedor',
            dataIndex: 'fornecedor',
            key: 'fornecedor',
            width: "15%",
            align: "center",
        }
    ];

    return (
        <div className="historico">
            <div className="voltar">
            <StyledButton  route="/historico" text="Voltar" colorbutton="purple"></StyledButton>
            </div>
            <h2>Relatório</h2>
            <div className='info-operacao'>
                <p><strong>Carrinho: </strong> {operacao.id_carrinho}</p>
                <p><strong>Responsável: </strong>{operacao.id_responsavel}</p>
                <p><strong>Operação: </strong>{operacao.tipo_operacao}</p>
                <p><strong>Data: </strong>{operacao.data && operacao.data.split(',')[0]}</p>
                <p><strong>Horário: </strong>{operacao.data && operacao.data.split(',')[1]}</p>
            </div>
            
            <Table 
            dataSource={relatorio} 
            columns={columns}
            align="center"
            headerBg={"#6A2FF5"}
            rowKey="id"  />
        </div>
    );  
}

export default Relatorio;
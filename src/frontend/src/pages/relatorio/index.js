import { useEffect, useState } from 'react';
import Axios from 'axios';
import { Table } from 'antd';
import { useNavigate } from 'react-router-dom';
import { useParams } from 'react-router-dom';

function Relatorio() {
	let id_operacao= useParams();	
    const navigate = useNavigate();
    const [relatorio, setRelatorio] = useState([]);

    useEffect(() => {
        const getRelatorio = async () => {
            try {
                const response = await Axios.get(`http://localhost:8000/bipagem/2`);
                console.log(response.data);
				const data = response.data;
				const groupedData = data.reduce((acc, curr) => {
					if (acc[curr.nome]) {
						acc[curr.nome].count += 1;
					} else {
						acc[curr.nome] = { ...curr, count: 1 };
					}
					return acc;
				}, {});
				setRelatorio(Object.values(groupedData));
				
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
            title: 'Lote',
            dataIndex: 'lote',
            key: 'lote',
            width: "15%",
            render: (text) => {
                const time = text.split(' ')[1];
                return <span>{time}</span>;
            },
            align: "center"
        },
        {
            title: 'Carrinho',
            dataIndex: 'id_carrinho',
            key: 'id_carrinho',
            width: "10%",
            align: "center",
        },
        {
            title: 'Tipo de Carrinho',
            dataIndex: 'tipo_carrinho',
            key: 'tipo_carrinho',
            width: "15%",
            align: "center",
        },
        {
            title: 'Responsável',
            dataIndex: 'id_responsavel',
            key: 'id_responsavel',
            width: "15%",
            align: "center",
        },
        {
            title: 'Operação',
            dataIndex: 'tipo_operacao',
            key: 'tipo_operacao',
            width: "15%",
            align: "center",
        },
        {
            title: 'Relatório',
            text: 'id_operacao',
            width: "20%",
            render: (text, record) => {
                return (
                    <button onClick={() => navigate(`/relatorio/${text.id_operacao}`)}>exibir PDF</button>
                );},
                align: "center",
        }
    ];

    return (
        <div className="historico">
            <h1>Histórico de Relatórios</h1>
            <Table 
            dataSource={relatorio} 
            columns={columns}
            align="center"
            headerBg={"#6A2FF5"} />
        </div>
    );  
}

export default Relatorio;
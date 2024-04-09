import "./historico.css"
import { useEffect, useState } from 'react';
import Axios from 'axios';
import { Table } from 'antd';
import { useNavigate } from 'react-router-dom';
import StyledButton from "../../components/styledButton";

function Historico() {
    const navigate = useNavigate();
    const [historico, setHistorico] = useState([]);

    useEffect(() => {
        const getHistorico = async () => {
            try {
                const response = await Axios.get('http://localhost:8000/operacoes/');
                console.log(response.data);
                setHistorico(response.data);
            } catch (error) {
                console.error(error);
            }
        };

        getHistorico();
    }, []);

    const columns = [
        {
            title: 'Data',
            dataIndex: 'data',
            key: 'data',
            width: "10%",
            render: (text) => {
                var date = text.split(' ')[0];
                if (date.endsWith(',')) {
                    date = date.slice(0, -1);
                }
                return <span>{date}</span>;
            },
            align: "center"
        },
        {
            title: 'Hora',
            dataIndex: 'data',
            key: 'data',
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
                    <StyledButton route={`/relatorio/${text.id_operacao}`} text="ver relatório" colorbutton="purple"></StyledButton>
                );},
                align: "center",
        }
    ];

    return (
        <div className="historico">
            <h1>Histórico de Relatórios</h1>
            <Table 
            dataSource={historico} 
            columns={columns}
            align="center"
            headerBg={"#6A2FF5"} />
        </div>
    );  
}

export default Historico;
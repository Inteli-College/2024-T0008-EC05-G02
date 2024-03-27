import Title from 'antd/es/skeleton/Title';
import StyledButton from '../../components/styledButton';
import './home.css';
import React from 'react';
import { useNavigate } from 'react-router-dom';

function Home() {
    const navigate = useNavigate();

    const handleCreateCart = () => {
        navigate('/criar');
    };

    const handleRefillCart = () => {
        navigate('/abastecer');
    };

    return (
        <div className="Home">
            <div className='home-logo'>
                <img src='/logo2x.png' alt="Logo" />
            </div>
            <div className='Title'>
                <h1 className='adAlma'>Ad Alma</h1>
                <h2 className='slogan'>Eficiência e segurança salvam vidas</h2>
            </div>
            <h2 style={{color:"black", fontWeight:"400"}}>Qual das operações você gostaria de realizar?</h2>
            <div className='home-botoes'>
                <StyledButton text="Criar carrinho" textColor="blue" onClick={handleCreateCart}></StyledButton>
                <StyledButton text="Abastecer carrinho" textColor="purple" onClick={handleRefillCart}></StyledButton>
            </div>
        </div>
    );
}

export default Home;
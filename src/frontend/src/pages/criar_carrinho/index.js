import React from 'react';
import './criar-carrinho.css';
import CreateForm from '../../components/form';
import {useNavigate} from 'react-router-dom';

export default function CriarCarrinho() {

    let navigate = useNavigate();
    return (
        <div className='criar-carrinho'>
            <CreateForm onFinish={() => console.log("zzzzz")}/>
        </div>
    );
}
import React from 'react';
import Axios from 'axios';
import './criar-carrinho.css';
import CreateForm from '../../components/form';
import {useNavigate} from 'react-router-dom';

export default function CriarCarrinho() {

    let navigate = useNavigate();
    return (
        <div className='criar-carrinho'>
            <CreateForm/>
        </div>
    );
}
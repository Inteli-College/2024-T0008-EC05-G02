import React from 'react';
import { Input, Select, Button } from 'antd';
import './form.css';

const { Option } = Select;

const CreateForm = () => {
  return (
    <div className="container">
      <div className="card">
        <h1 className="title">Criar carrinho</h1>
        <h1 className="subTitle">Preencha as informações abaixo para iniciar a bipagem</h1>
        <div className="field">
          <Input placeholder="Responsável" />
        </div>
        <div className="field">
          <Input placeholder="Área de atuação" />
        </div>
        <div className="field">
          <Select placeholder="Tipo de carrinho" style={{ width: '100%' }}>
            <Option value="tipo1">Tipo 1</Option>
            <Option value="tipo2">Tipo 2</Option>
            {/* Outras opções */}
          </Select>
        </div>
        {/* Outras opções */}
      </div>
    </div>
  );
};

export default CreateForm;

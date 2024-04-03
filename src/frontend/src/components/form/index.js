import React, { useState } from 'react';
import Axios from 'axios';
import './form.css';
import { Select, Form, Input} from 'antd';
import StyledButton from '../styledButton';
import { useNavigate } from 'react-router-dom';



function CreateForm() {
  const [form, setForm] = useState({});
  const currentDate = new Date().toLocaleString("pt-BR", {timeZone: "America/Sao_Paulo"});
  const navigate = useNavigate();

  const submitForm = async () => {
    // console.log("Forms values:")
    // console.log(form);

    const formData = {
      ...form,
      "id_responsavel": parseInt(form.id_responsavel),
      "id_carrinho": parseInt(form.id_carrinho),
      "data": currentDate,
      // "tipo_operacao": form.tipo_operacao,
      "tipo_operacao": "criar",
      "tipo_carrinho": form.tipo_carrinho
    }

    console.log(formData);

    try {
        const response = await Promise.all([
        
        Axios.post('http://localhost:8000/adicionar_operacao', formData),
        Axios.get('http://127.0.0.1:5000/demonstracao' )])
        console.log(response.data);
    } catch (error) {
        alert(error);
    }
    navigate('/bipagem');
  }

  return (
  <div className='forms-carrinho'>
  <h3>Preencha as informações abaixo para iniciar a bipagem:</h3>
  <Form
  labelWrap
  labelAlign='left'
    wrapperCol={{
      span: 20,
      offset: 1,
    }}
    initialValues={{
      remember: true,
    }}
    style={{padding: '12px'}}
    onFinish={submitForm}
    autoComplete="off"
  >
    <Form.Item
      label="Responsável"
      name="id_responsavel"
      rules={[
        {
          required: true,
          message: 'Por favor insira o nome do responsável pela operação!',
        },
      ]}
    >
      <Select
      options={
       [ {label:'Luiza', 'value':'1'},
        {label:'João', 'value':'2'},
        {label:'Maria', 'value':'3'},
        {label:'José', 'value':'4'}, 
        {label:'Ana', 'value':'5'}]
      }
      onChange={(value)=> setForm({...form, "id_responsavel": value})}
      />
    </Form.Item>
    <Form.Item
      label="Tipo de Carrinho"
      name="type"
      rules={[
        {
          required: true,
          message: 'Insira o tipo de carrinho!',
        },
      ]}
    >
      <Select
      options={[
        { value: 'Infantil', label: 'Infantil' },
        { value: 'Adulto', label: 'Adulto' },
      ]}
      onChange={(value)=> setForm({...form, "tipo_carrinho": value})}
      />
    </Form.Item>
    <Form.Item
      label="Insira o ID do carrinho"
      name="car_id"
      rules={[
        {
          required: true,
          message: 'Por favor insira o id do carrinho a ser criado!',
        },
      ]}
      onChange={(value)=> setForm({...form, "id_carrinho": value.target.value})}
    >
      <Input />
    </Form.Item>
    <Form.Item
    >
      <StyledButton type="primary" htmlType="submit" text="iniciar bipagem" colorbutton="green" onClick={submitForm}>
        Submit
      </StyledButton>
    </Form.Item>
  </Form>
  </div>
)
}
export default CreateForm;
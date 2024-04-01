import React from 'react';
import Axios from 'axios';
import {Checkbox, Form, Input, InputNumber, Select } from 'antd';
import StyledButton from '../styledButton';


// const onFinish = (values) => {
//   console.log('Success:', values);};

function CreateForm(props) {
  const [varrer, setVarrer] = React.useState(false);

  const handleVarrerClick = () => {
    setVarrer(true);
  }

  // const handleIniciarBipagem = async (values) => {
  //   console.log('Success:', values);
  //   try {
  //     // Assuming 'values' is an object with keys and values you want to send as query parameters
  //     // Construct query parameters from 'values'
  //     const queryParams = new URLSearchParams(values).toString();
  
  //     // Append the query parameters to your endpoint
  //     const response = await Axios.get(`your_api_endpoint?${queryParams}`);
  
  //     console.log(response.data);
  //     // Optionally, do something with the response data, like redirecting the user
  //     // For example, if you want to redirect to another route on success:
  //     // props.history.push('/bipagem-finalizada');
  //   } catch (error) {
  //     console.error('There was an error!', error);
  //   }
  // };
  

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
    onFinish={props.onFinish}
    autoComplete="off"
  >
    <Form.Item
      label="Responsável"
      name="owner"
      rules={[
        {
          required: true,
          message: 'Por favor insira o nome do responsável pela operação!',
        },
      ]}
    >
      <Input />
    </Form.Item>

    <Form.Item
      label="Área de atuação"
      name="area"
      rules={[
        {
          required: true,
          message: 'Insira a área de atuação!',
        },
      ]}
    >
      <Select
      options={[
        { value: 'Emergência', label: 'Emergência' },
        { value: 'Enfermaria', label: 'Enfermaria' },
      ]}
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
      />
    </Form.Item>
    <Form.Item
      label="Qtd. colunas de compartimento da bandeja"
      name="columns"
      rules={[
        {
          required: true,
          message: 'Por favor insira a quantidade de colunas de compartimento da bandeja!',
        },
      ]}
    >
      <InputNumber />
    </Form.Item>
    <Form.Item
      label="Qtd. linhas de compartimento da bandeja"
      name="rows"
      rules={[
        {
          required: true,
          message: 'Por favor insira a quantidade de linhas de compartimento da bandeja!',
        },
      ]}
    >
      <InputNumber />
    </Form.Item>
    <Form.Item
    >
      <StyledButton route="/em-conformidade" type="primary" htmlType="submit" text="iniciar bipagem" colorbutton="green" 
      // onClick={handleIniciarBipagem}
      >
        Submit
      </StyledButton>
    </Form.Item>
  </Form>
  </div>
)
}
export default CreateForm;
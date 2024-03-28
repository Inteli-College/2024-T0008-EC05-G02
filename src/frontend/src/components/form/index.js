import React from 'react';
import {Checkbox, Form, Input, InputNumber, Select } from 'antd';
import StyledButton from '../styledButton';


const onFinish = (values) => {
  console.log('Success:', values);};

function CreateForm() {
  const [varrer, setVarrer] = React.useState(false);

  const handleVarrerClick = () => {
    setVarrer(true);
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
    onFinish={onFinish}
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
      <StyledButton onClick={handleVarrerClick} text="verificar bandeja" colorbutton="yellow">
        Submit
      </StyledButton>
      <StyledButton type="primary" htmlType="submit" text="iniciar bipagem" colorbutton="green" >
        Submit
      </StyledButton>
    </Form.Item>
  </Form>
  </div>
)
}
export default CreateForm;
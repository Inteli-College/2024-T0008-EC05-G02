import './App.css';
import CreateForm from './components/form';
import './components/drugCard/drug-card.css';
import atom from './components/drugCard/atom.png';
import React from 'react';

import { Checkbox, Input, Button } from 'antd';

// const onFinish = (values) => {
//   console.log('Success:', values);
// };
// const onFinishFailed = (errorInfo) => {
//   console.log('Failed:', errorInfo);
// };

function App() {
  return (
    <div className="App">
      <Input placeholder="Basic usage"/>
      {/* <DrugCard 
        drug={{
          status: "Em conformidade",
          name: "Paracetamol",
          dose: "500mg",
          expiration: "10/10/2022",
          batch: "123456",
          supplier: "Farmacia",
          color: "green",
          image: atom
        }}
        /> */}
        
      {/* <Form
    name="basic"
    labelCol={{
      span: 8,
    }}
    wrapperCol={{
      span: 16,
    }}
    style={{
      maxWidth: 600,
    }}
    initialValues={{
      remember: true,
    }}
    // onFinish={onFinish}
    // onFinishFailed={onFinishFailed}
    autoComplete="off"
  >
    <Form.Item
      label="Username"
      name="username"
      rules={[
        {
          required: true,
          message: 'Please input your username!',
        },
      ]}
    >
      <Input />
    </Form.Item>

    <Form.Item
      label="Password"
      name="password"
      rules={[
        {
          required: true,
          message: 'Please input your password!',
        },
      ]}
    >
      <Input.Password />
    </Form.Item>

    <Form.Item
      name="remember"
      valuePropName="checked"
      wrapperCol={{
        offset: 8,
        span: 16,
      }}
    >
      <Checkbox>Remember me</Checkbox>
    </Form.Item>

    <Form.Item
      wrapperCol={{
        offset: 8,
        span: 16,
      }}
    >
      <Button type="primary" htmlType="submit">
        Submit
      </Button>
    </Form.Item>
  </Form> */}

    </div>
  );
}

export default App;

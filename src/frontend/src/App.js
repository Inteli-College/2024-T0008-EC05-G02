import './App.css';
import CreateForm from './components/form';
import './components/form/form.css';
import './components/drugCard/drug-card.css';
import atom from './components/drugCard/atom.png';
import React from 'react';

import { Button, Checkbox, Form, Input } from 'antd';

// const onFinish = (values) => {
//   console.log('Success:', values);
// };
// const onFinishFailed = (errorInfo) => {
//   console.log('Failed:', errorInfo);
// };

function App() {
  return (
    <div className="App">
      <CreateForm />
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
    </div>
  );
}

export default App;

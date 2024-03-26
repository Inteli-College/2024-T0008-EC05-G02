import React from 'react';
import './App.css';
import CreateForm from './components/form';
import './components/drugCard/drug-card.css';
import atom from './components/drugCard/atom.png';
import React from 'react';
import NavBar from './components/menu/navbar.js';

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
      <NavBar />
      {CreateForm}
      <CreateForm />
      <div className='divButton'>
        <Button className='buttonBandeja button'>Verificar Bandeja</Button>
        <Button className='buttonBipagem button'>Iniciar Bipagem</Button>
      </div>
      <footer>
        Desenvolvido pelo Grupo (AdAlma) - Inteli - Instituto de Tecnologia e Liderança
      </footer>
    </div>
  )
}

export default App;



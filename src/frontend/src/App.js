import React from 'react';
import './App.css';
import CreateForm from './components/form';
import NavBar from './components/menu/navbar.js';
import { Button } from 'antd';


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
  );
}

export default App;

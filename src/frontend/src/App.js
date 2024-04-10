import './App.css';
import React from 'react';
import NavBar from './components/menu';
import Home from './pages/home';
import MedicamentoConformidade from './pages/medicamentos-conformidade';
import CriarCarrinho from './pages/criar_carrinho';
import ManualInstrucoes from './pages/manual';
import Historico from './pages/historico';
import Relatorio from './pages/relatorio';
import BipagemIncompletaFinalizada from './pages/bipagem_finalizada_incompleta';
import BipagemFinalizada from './pages/bipagem-finalizada';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';

function App() {
  return (

    <Router>
      
      <div className="App">
        <NavBarWrapper />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/manual" element={<ManualInstrucoes/>} />
         <Route path="/criar" element={<CriarCarrinho />} />
         <Route path="/abastecer" element={<div>abastecer carrinho</div>} />
         <Route path="/historico" element={<Historico />} />
         <Route path="/bipagem" element={<MedicamentoConformidade />} />
         <Route path="/fim-bipagem-incompleta:id_operacao" element={<BipagemIncompletaFinalizada />} />
         <Route path="/fim-bipagem" element={<BipagemFinalizada />} />
         <Route path='/relatorio/:id_operacao' element={<Relatorio/>} />
        </Routes>
        <div className="footer">Desenvolvido pelo Grupo 2 Inteli - Instituto de Tecnologia e Liderança</div>
      </div>
    </Router>
  );
}

function NavBarWrapper() {
  const navigate = useNavigate();

  const handleMenuClick = (route) => {
    navigate(`/${route}`);
  };

  return <NavBar onMenuClick={handleMenuClick} />;
}

export default App;



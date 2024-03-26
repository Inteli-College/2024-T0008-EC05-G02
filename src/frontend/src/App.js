import './App.css';
import React from 'react';
import NavBar from './components/menu';
import Home from './pages/home';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';


// function App() {
//   const navigate = useNavigate();

//   const handleMenuClick = (route) => {
//     <Route>navigate(`/${route}`);</Route>

//   };

//   return (
//     <div className='App'>
//       <NavBar onMenuClick={(route)=>handleMenuClick(route)}/>
//       <Router>
//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/manual" element={<React.Menu />} />
//         <Route path="/criar" element={<React.Input />} />
//         <Route path="/abastecer" element={<React.Dropdown />} />
//         <Route path="/historico" element={<React.Select />} />
//       </Routes>
//     </Router>
//     </div>
//   );
// }

// export default App;

function App() {
  return (
    <Router>
      <div className="App">
        <NavBarWrapper />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/manual" element={<div>manual</div>} />
         <Route path="/criar" element={<div>criar carrinho</div>} />
         <Route path="/abastecer" element={<div>abastecer carrinho</div>} />
         <Route path="/historico" element={<div>historico</div>} />
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



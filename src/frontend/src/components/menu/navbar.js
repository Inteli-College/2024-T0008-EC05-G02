import React, { useState } from 'react';
import { Menu } from 'antd';
import './menubar.css';
import logo from './logo.png'; 

const items = [
  {
    label: (
      <div className='divLogo'>
        <img src={logo} alt="Logo" style={{ width: '40px', height: '40px', marginRight: '50px', alignSelf: 'center' }} />
        
      </div>
    ),
    
  },

  {
    label: 'Manual de Instruções',
    key: 'manual',
  },
  {
    label: 'Criar Carrinho',
    key: 'criar',
  },
  {
    label: 'Abastecer Carrinho',
    key: 'abastecer',
  },
  {
    label: 'Histórico de Relatórios',
    key: 'historico',
  },
];

const NavBar = () => {
  const [current, setCurrent] = useState('manual');

  const onClick = (e) => {
    setCurrent(e.key);
  };

  return (
    <div className='pageBody'>
      <Menu
        onClick={onClick}
        selectedKeys={[current]}
        mode="horizontal"
        items={items}
        className="menu-fixed-top"
      />
    </div> 
  );
};

export default NavBar;

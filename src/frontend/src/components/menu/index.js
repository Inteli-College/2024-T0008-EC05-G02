import React, { useState } from 'react';
import { Menu } from 'antd';
import './menubar.css';
import logo from './logo.png'; 

const items = [
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
      <div className='header-group'>
      <img className="logo" src={logo} alt="Logo" />
      <Menu
        onClick={onClick}
        horizontalItemSelectedBg='#EBF5FD'
        horizontalItemHoverBg='#F2F2F2'
        selectedKeys={[current]}
        mode="inline"
        items={items}
        
        className="menu-fixed-top"
      />
      </div>
      {/* <div className='colorful-bar'></div> */}
    </div> 
  );
};

export default NavBar;

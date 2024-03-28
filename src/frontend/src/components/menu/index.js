import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Menu } from 'antd';
import './menubar.css';
import logo from './logo.png'; 

const items = [
  {
    label: 'Manual de Instruções',
    key: "manual",
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

const NavBar = ({onMenuClick}) => {
  const [current, setCurrent] = useState("");

  const onClick = (e) => {
    setCurrent(e.key);
    return onMenuClick(e.key);
  };

  return (
    <div className='pageBody'>
      <div className='header-group'>
      <Link to="/">
          <img className="logo" src={logo} alt="Logo"/>
        </Link>
      <Menu
        onClick={onClick}
        selectedKeys={[current]}
        mode="inline"
        items={items}
        inlineIndent={0}
        className="menu-fixed-top"
      />
      </div>
      <div className='colorful-bar'></div>
    </div> 
  );
};

export default NavBar;

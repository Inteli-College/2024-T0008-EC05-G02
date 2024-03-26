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

    </div>
  );
}

export default App;

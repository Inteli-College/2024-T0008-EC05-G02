import './App.css';
import CreateForm from './components/form';
import './components/form/form.css';
import './components/drugCard/drug-card.css';
import atom from './components/drugCard/atom.png';
import React from 'react';

import { Button, Checkbox, Form, Input } from 'antd';
import Home from './pages/home';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';  
import About from './pages/about';
import Contact from './pages/contact';

// const onFinish = (values) => {
//   console.log('Success:', values);
// };
// const onFinishFailed = (errorInfo) => {
//   console.log('Failed:', errorInfo);
// };

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/about" component={About} />
          <Route path="/contact" component={Contact} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;

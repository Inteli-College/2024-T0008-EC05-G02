import './App.css';
import React from 'react';

import Home from './pages/home';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';  


export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        {/* Add more rotes as needed */}
      </Routes>
    </Router>
  );
}
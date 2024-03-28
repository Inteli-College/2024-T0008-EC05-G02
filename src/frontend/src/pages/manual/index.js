import React from 'react';
import { Anchor, Row, Col } from 'antd';
import './style.css';

const Indice = () => (
    <Row>
      <Col span={16}>
        <div
          id="part-1"
          style={{
            height: '100vh',
            background: 'rgba(255,0,0,0.02)',
          }}
        />
        <div
          id="part-2"
          style={{
            height: '100vh',
            background: 'rgba(0,255,0,0.02)',
          }}
        />
        <div
          id="part-3"
          style={{
            height: '100vh',
            background: 'rgba(0,0,255,0.02)',
          }}
        />  
        <div
          id="part-4"
          style={{
            height: '100vh',
            background: 'rgba(0,0,255,0.02)',
          }}
        />
      </Col>
      <Col span={8}>
        <Anchor
          items={[
            {
              key: 'part-1',
              href: '#part-1',
              title: 'Introdução',
            },
            {
              key: 'part-2',
              href: '#part-2',
              title: 'Criar',
            },
            {
              key: 'part-3',
              href: '#part-3',
              title: 'Abastecer',
            },
            {
              key: 'part-4',
              href: '#part-4',
              title: 'Itens faltantes',
            }
          ]}
        />
      </Col>
    </Row>
  );

function ManualInstrucoes() {
    return (
        <div className="manual">
          <h1>Manual de Instruções</h1>
          <div id="menu">
            <ul id="indice">
              <Indice/>
            </ul>
          </div>
          <div className="header" id="header1">
            <h2>Introdução</h2>
            <p>
              
            </p>
          </div>
          <div className="header" id="header2">
            <h2>Criar</h2>
            <p>
              
            </p>
          </div>
          <div className="header" id="header3">
            <h2>Abastecer</h2>
            <p>
              
            </p>
          </div>
          <div className="header" id="header4">
            <h2>Itens Faltantes</h2>
            <p>
            
            </p>
        </div>
      </div>
      );
}

export default ManualInstrucoes;
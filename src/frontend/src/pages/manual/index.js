import React from 'react';
import { Anchor, Row, Col } from 'antd';
import './style.css';

const Indice = () => (
    <Row>
      <Col >
        <div
          id="part-1"
          style={{
            height: '100vh',
            background: 'rgba(255,0,0,0.02)'
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
      <Col >
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
            // {
            //   key: 'part-3',
            //   href: '#part-3',
            //   title: 'Abastecer',
            // },
            {
              key: 'part-3',
              href: '#part-3',
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
          <div id="conteudo">
          <h1>Manual de Instruções</h1>
          <div className="header" id="header1">
            <h2>Introdução</h2>
            <p>
              Bem-vindo ao Manual de Instruções. Este documento fornece orientações detalhadas sobre como usar a interface para gerenciar carrinhos, abastecer medicamentos e realizar bipagem. <br></br> <br></br>

              Leia atentamente as instruções fornecidas para aproveitar ao máximo o sistema.

            </p>
          </div>
          <div className="header" id="header2" href="#part-2">
            <h2>Criar carrinho</h2>
            <p>
              Para criar um novo layout para o carrinho, siga estas etapas: <br></br> <br></br>

              1. Na página inicial, clique em "Criar Carrinho". <br></br>
              2. Preencha os campos necessários, como tipo do carrinho e informações do responsável. <br></br>
              3. Clique em "Iniciar Bipagem" e aguarde o robô se movimentar.

            </p>
          </div>
          {/* <div className="header" id="header3" href="#part-3">
            <h2>Abastecer</h2>
            <p>
              Para criar um novo layout para o carrinho, siga estas etapas: <br></br> <br></br>

              1. Na página inicial, clique em "Abastecer Carrinho". <br></br>
              2. Preencha os campos necessários, como tipo do carrinho e informações do responsável. <br></br>
              3. Clique em "Iniciar Bipagem" e aguarde o robô se movimentar.

            </p>
          </div> */}
          <div className="header" id="header4" href="#part-3">
            <h2>Itens Faltantes</h2>
            <p>
              Nossa interface oferece recursos robustos de relatórios. Veja como acessá-los: <br></br> <br></br>

              1. Navegue até a seção de relatórios. <br></br>
              2. Selecione o tipo de relatório desejado. <br></br>
              3. Visualize, exporte ou imprima os relatórios conforme necessário. <br></br>
            </p>
        </div>
      </div>
      <div id="menu">
            <div id="indice">
              <Indice/>
            </div>
          </div>
    </div>
      );
}

export default ManualInstrucoes;
---
sidebar_label: 'Experiência do Usuário'
sidebar_position: 2
---

# Experiência do Usuário

Abaixo se encontram documentos do Entendimento do **Usuário** referentes à Sprint 1. Eles auxiliam em uma melhor compreensão do usuário, suas dores e fluxo na solução. 
<!-- Escreva embaixo de cada título com '##' -->

## Imersão Preliminar

**Introdução**

A pesquisa preliminar tem como objetivo principal definir o escopo do projeto realizado em colaboração entre o grupo Ad Alma e a empresa Sírio Libanês, com foco na área de farmácia. Adicionalmente, busca-se compreender as restrições, necessidades e pontos críticos do projeto, assim como entender o contexto empresarial e setorial pertinentes. Além disso, pretende-se analisar a interação dos usuários com a solução, compreender seu impacto e extrair as informações necessárias para elaborar um projeto que atenda plenamente aos requisitos estabelecidos.

A pesquisa é fundamental para o sucesso do projeto, pois permite a coleta de dados essenciais para o seu desenvolvimento. Isso possibilita a construção de um projeto que esteja alinhado com as necessidades dos usuários desde o início, reduzindo significativamente o risco de desenvolver uma solução que não atenda às expectativas do cliente. Além disso, a pesquisa preliminar contribui para a identificação precoce de possíveis problemas e desafios, o que permite ajustes e correções antes mesmo do início efetivo do projeto. Dessa forma, investir tempo e recursos em uma pesquisa preliminar robusta é fundamental para garantir o sucesso e a eficácia do design system.

Para direcionar e executar a pesquisa de forma eficiente e atingir o objetivo proposto, o grupo optou por se aprofundar nos documentos fornecidos, participar do kick-off com os parceiros e conduzir uma sessão de perguntas subsequente. Além disso, na etapa de pesquisa desk, o foco foi explorar tópicos relacionados aos temas destacados na pesquisa exploratória, utilizando o Google Acadêmico para encontrar artigos que pudessem contribuir para o desenvolvimento do projeto.


**Pesquisa exploratória**

A pesquisa exploratória foi conduzida por meio de dois eventos principais realizados no INTELI - Instituto de Tecnologia e Liderança: o Kick-off com os stakeholders (Conrad e Lorena) e uma sessão de perguntas sobre o projeto com um dos stakeholders (Lorena).
O Kick-off, realizado às 14h do dia 05/02/2024, contou com a participação dos parceiros do projeto, os quais apresentaram de forma expositiva informações sobre a empresa e o projeto aos estudantes presentes, por meio de uma apresentação de slides. Esta atividade possibilitou a coleta das primeiras informações sobre a empresa e o projeto, além de esclarecer dúvidas iniciais que surgiram durante a apresentação.

Dois dias depois, em 07/02/2024 às 16h, ocorreu a sessão de perguntas, exclusivamente com a participação da parceira (Lorena). A sessão foi estruturada de modo que a parceira estava no centro e respondia a perguntas pré-elaboradas pelos estudantes, garantindo que todas as respostas fossem audíveis para todos os presentes. As perguntas feitas podem ser acompanhadas no apêndice A, fixado no fim da pesquisa preliminar.

Todas as informações obtidas durante esses dois eventos foram registradas em formato textual, e todas as informações diretamente fornecidas pelos parceiros foram compartilhadas com os alunos para futuras consultas.

A partir das informações coletadas, foi possível definir melhor o escopo do projeto, em relação ao que é esperado e como deve ser desenvolvido. Para uma compreensão mais detalhada das informações extraídas, dividimos a pesquisa em três partes distintas:

1. Informações pré-estabelecidas:
    Antes dos eventos de esclarecimento do escopo, os estudantes já estavam cientes de que iriam desenvolver a automação do processo de montagem de carrinhos de emergência do Hospital Sírio Libanês. Além disso, foi possível obter informações sobre o problema atual do setor, os objetivos e o escopo macro da solução, bem como as restrições gerais por meio da TAPI do projeto. Dentre as principais informações extraídas do arquivo, destacam-se:
     - Os benefícios esperados pela solução: "redução no tempo para montagem dos carrinhos de emergência e relatórios dos itens utilizados (API/Visualização)."
     - O problema que deve ser resolvido: "facilitar a rotina de montagem dos carrinhos de emergência."
     - As necessidades que devem ser atendidas: considerar os diferentes layouts dos carrinhos para a automação e para o sistema (API); integrar com o sistema do hospital; possibilitar o rastreamento dos medicamentos dentro do carrinho.
     - As restrições do projeto: o projeto deve se limitar a um braço robótico em escala reduzida para a prova de conceito; o projeto não contempla integração com sistemas de logins; as tecnologias utilizadas estarão dentro do escopo do módulo estabelecido pela instituição.

2. Informações do Kick-off:
   - Durante o kick-off, foram apresentadas informações sobre a história da empresa, seus valores institucionais e a operação da farmácia do hospital, incluindo o processo de montagem dos carrinhos de emergência atualmente utilizado. Durante a apresentação, foram destacados os desafios e oportunidades de melhoria no processo atual.

3. Informações da roda de perguntas:
    Durante a roda de perguntas, foram extraídas diversas informações complementares que esclareceram o contexto da solução e como deve ser executada, sendo possível extrair as seguintes informações:
     Em relação aos usuários e ao que é esperado:
        - Os principais usuários são: o auxiliar de farmácia (cuida de forma direta da montagem) com uma faixa etária de 20-30 anos, o médico ou enfermeiro (que utiliza o carrinho após a montagem) com uma faixa etária de 30-60 anos, e o paciente (que se beneficia da solução, mas não a utiliza de forma direta).
        - O principal ganho que a solução pode oferecer é em relação ao tempo gasto, principalmente em relação ao processo de bipagem, que é hoje o mais demorado e com maior chances de erro. Além disso, existem outros problemas na forma manual como é realizado o processo hoje, como por exemplo: a possibilidade de erro humano ao colocar o medicamento em um lugar errado, ou bipar o mesmo código de medicamento várias vezes.
        - O maior desafio para a solução proposta é que ela pode esbarrar na demanda de confiabilidade para o processo. Ela deve agregar valor trazendo mais segurança e de forma alguma reduzindo o padrão de segurança atual".
     Configuração dos carrinhos:
        - Os carrinhos apresentam duas categorias diferentes com suas especificidades (o adulto e o pediátrico). Além disso, existem diversos layouts diferentes e com dimensões distintas por terem sido adquiridos em tempos diferentes pelo hospital.
        - A organização em si é pré-definida, dependendo de cada layout cada medicamento deve estar em uma posição diferente.
     Em relação a solução e ao processo de bipagem:
        - Os bips dos medicamentos são feitos no momento de abastecimento do carrinho e cobram o que foi utilizado pela diferença (ou seja, aqueles códigos não bipados foram utilizados). É necessário que todos os medicamentos sejam bipados para garantir a rastreabilidade e a verificação dos vencimentos.
        - Existem dois momentos principais em que o robô pode atuar: verificação do vencimento que ocorre todo o mês e abastecimento do carrinho após o uso.
        - É necessário integrar o banco de dados na solução.
     Em relação ao kit:
        - Além do carrinho, outro possível objeto de desenvolvimento é o kit de emergência. O kit apresenta menos itens em sua composição e menor quantidade de possíveis layouts em relação ao carrinho. Em relação ao processo de montagem, é similar à forma como é feita com o carrinho de emergência.

    Com base na pesquisa exploratória realizada, foram identificados os principais insights para o grupo, incluindo:

     - A importância de aprimorar o processo de bipagem dos itens, visando assegurar a rastreabilidade do sistema.
a necessidade de configurar a solução para lidar com diferentes layouts de gavetas dos carrinhos, podendo essa funcionalidade ser incorporada à própria API.
     - A relevância de realizar testes que comprovem a segurança da automação, garantindo que não haja riscos para os operadores nem para os pacientes do hospital.
     - A importância de considerar dois fluxos distintos: um para a verificação do prazo de validade dos itens e outro para o reabastecimento dos carrinhos.
     - A possibilidade de integrar a verificação do prazo de validade no momento do reabastecimento.



**Pesquisa Desk**

Durante a condução da pesquisa desk, o grupo concentrou-se em aprimorar a compreensão do contexto da solução e identificar projetos similares em andamento. Um dos parâmetros cruciais foi a investigação do avanço da tecnologia e da Indústria 4.0 na área da saúde, destacado em um trabalho de conclusão de curso de um estudante da UNIFESP em 2021. Esse estudo permitiu compreender a relevância da automatização em termos de redução de custos, exemplificada por um hospital piloto que alcançou uma diminuição de 65% nos custos por hora de trabalho para tarefas simples. Além disso, observou-se como essa automação pode otimizar o tempo da equipe de enfermagem, possibilitando uma maior interação com os pacientes.

Outro ponto enfatizado foi a necessidade de personalização das soluções de automatização para cada contexto hospitalar específico, uma vez que as necessidades variam de acordo com a organização, processos, estrutura física e especialidades médicas.

No que diz respeito a projetos relacionados que podem servir como referência, em 2017, uma dupla de alunas da Escola Politécnica da USP desenvolveu um projeto de conclusão de curso intitulado "Automação do processo de conferência dos itens de carros de emergência em um hospital". Esse projeto, similar ao nosso, fornece insights valiosos que podem ser utilizados como referência, especialmente destacando os pontos de atenção identificados nos testes. Por exemplo, a dificuldade em ler etiquetas compostas por metal ou quando estas estão sobrepostas, evidenciando a importância de um sistema de verificação de códigos robusto, independentemente da tecnologia utilizada.

Além disso, a dissertação proporcionou um entendimento mais profundo sobre a integração entre hardware, banco de dados e API, aspectos essenciais que serão implementados na solução.

A partir das informações coletadas, destacaram-se dados cruciais para o desenvolvimento do projeto, tais como:
a necessidade de antecipar potenciais problemas no processo de bipagem ou escaneamento dos códigos dos itens e estar preparado para reverter esses erros de maneira eficiente.
a importância de compreender os fluxos e a integração do braço robótico, da API e do banco de dados em relação às funcionalidades do sistema.
a relevância de considerar o contexto específico do Hospital Sírio Libanês e como o sistema será implementado na área de farmácia já existente.


O método utilizado para pesquisar, definir e coletar os dados, consistiu em buscar temas relacionados ao projeto, como tecnologia, Indústria 4.0 e automação na área da saúde, por meio do Google Acadêmico, filtrando uma gama maior de textos confiáveis. Quanto às fontes utilizadas e escolhidas, considerou-se que as pesquisas acadêmicas citadas anteriormente são confiáveis sobre o assunto, uma vez que envolvem o esforço não só de estudantes das melhores universidades de São Paulo (UNIFESP e USP), mas também contam com referências e a aprovação de orientadores comprometidos com o corpo acadêmico e com experiência nas respectivas áreas tratadas. Para eventuais necessidades de especificação, as fontes utilizadas podem ser verificadas nas referências bibliográficas do projeto ou clicando nos links fornecidos acima.

**Apêndice A**

Perguntas feitas pelo grupo Ad Alma para a parceira:

Quantos layouts diferentes existem? Como eles se distribuem entre as categorias do carrinho (adulto e infantil)? Há a necessidade de se criar muitos layouts de forma recorrente? 
Os carrinhos são montados do zero? Ou também é preciso repor medicamentos pelo robô? 
Como vocês esperam que a nossa solução tenha compatibilidade com o sistema de vocês?
Como vocês imaginam o fluxo da  montagem dos carrinhos de emergência com a automação?. Vocês imaginam onde a parte de rastreabilidade dos medicamentos está inclusa nesse fluxo?  
Os carrinhos são montados por demanda ou existe uma quantidade definida de carrinhos que devem estar de prontidão? 

## Definição das Personas
## Jornada do Usuário

O Mapa de Jornada do Usuário fornece uma narrativa clara e organizada das experiências, sentimentos, pontos de dor e pontos de satisfação de um usuário ao longo de um processo.

Abaixo se encontram os mapas referentes a cada uma das personas: auxiliar de enfermagem e gerente de estoque. Tentamos mapear o fluxo geral que os usuários vão ter ao acessar a nossa plataforma e ter contato com o robô para automação.

### Jornada - Laís: Auxiliar de Enfermagem
![Jornada - Laís: Auxiliar de Enfermagem](../../static/img/jornada_lais.png)

### Jornada - João: Gerente de Estoque
![Jornada - João: Gerente de Estoque](../../static/img/jornada_joao.png)

Ambos documentos podem ser observados atráves deste [link.](https://miro.com/app/board/uXjVNr1y_C0=/?share_link_id=190601990822)

## User Stories


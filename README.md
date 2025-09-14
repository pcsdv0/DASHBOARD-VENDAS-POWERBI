
#  Dashboard Interativo de Vendas com Python, MySQL e Power BI

Projeto desenvolvido por **Paulo César**, estudante de Sistemas de Informação, com foco em soluções que integram **automação de dados, análise e visualização interativa**. Esta aplicação simula um ambiente de vendas reais, integrando **Python**, **MySQL** e **Power BI**, com o objetivo de transformar dados em insights de valor.

##  Destaques deste Projeto

- Integração prática entre Python, MySQL e Power BI
- Geração automática de dados realistas com a biblioteca Faker
- Indicadores de desempenho (KPIs) visuais e interativos
- Projeto replicável com instruções passo a passo
- Aplicável em ambientes comerciais reais



##  O que tem neste repositório?

- `gerar_dados.py`: Script em Python para gerar 500 registros fictícios de vendas e inserir no MySQL.
- `GRÁFICOS.pbix`: Arquivo do Power BI com o dashboard interativo e medidas em DAX.
- `EXEMPLO.png`: Imagem ilustrativa do resultado final do painel.
- `README.md`: Este arquivo de documentação explicando tudo que o projeto faz e como utilizá-lo.



##  Tecnologias Utilizadas

- **Power BI Desktop** — Visualização de dados
- **Python 3.x + Faker** — Geração automática de dados
- **MySQL** — Banco de dados relacional
- **Visual Studio Code** — Editor de código (opcional)
- **Git + GitHub** — Versionamento e portfólio público



## Funcionalidades do Dashboard

- ✅ **Faturamento Total** (soma das vendas)
- ✅ **Ticket Médio** (valor médio por venda)
- ✅ **Gráfico de Colunas** (vendas por mês)
- ✅ **Gráfico de Pizza** (vendas por categoria: Brinquedos, Presentes, Acessórios)
- ✅ **Filtros interativos** (por data, mês e categoria)



##  Como Reproduzir o Projeto

### 1. Configure o MySQL
Crie o banco de dados e a tabela `vendas` com o seguinte comando:


CREATE DATABASE vendas_dashboard;

USE vendas_dashboard;

CREATE TABLE vendas (
  OrderID INT,
  Date DATE,
  Category VARCHAR(50),
  Amount DECIMAL(10,2),
  Units INT
);


### 2. Gere os dados com Python
Instale o pacote necessário e execute o script:


pip install faker mysql-connector-python
python gerar_dados.py


O script vai gerar 500 vendas fictícias e inseri-las automaticamente no banco MySQL.


### 3. Conecte o Power BI ao MySQL
Abra `GRÁFICOS.pbix` no Power BI Desktop e selecione:

Obter Dados -> Banco de Dados MySQL

Informe os dados da sua conexão e carregue a tabela `vendas`.


##  Objetivo do Projeto

Este projeto foi criado com fins **educacionais e profissionais**, e é ideal para:

- Demonstrar domínio em integração de dados reais com Power BI
- Praticar automação com Python e banco de dados relacional
- Criar visualizações úteis para **tomada de decisão em vendas**


 **Este projeto demonstra minha capacidade de integrar dados e gerar insights visuais com foco em negócios. Estou aberto a oportunidades de estágio, parceria ou projetos. Entre em contato!**

🔗 Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/paulocvasconcelos) ou veja outros projetos no meu [GitHub](https://github.com/pcsdv0).

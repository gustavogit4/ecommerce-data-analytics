📦 E-commerce Data Analytics — Arquitetura e Pipeline de Dados

Autor: Gustavo de Paula Silva
Última atualização: Outubro/2025

Este projeto implementa um ambiente completo de engenharia e análise de dados para um e-commerce fictício, cobrindo todo o ciclo de vida da informação — da geração ao consumo analítico. A solução integra Python, SQLite e Power BI, com foco em arquitetura, transformação, automação e visualização.

1. Objetivo do Projeto

Desenvolver um pipeline de dados funcional que simula o fluxo real de trabalho em um ambiente de BI/Análise de Dados, incluindo:

geração de dados sintéticos realistas

armazenamento relacional

transformação e métricas de negócio

automação de rotinas

visualização dinâmica em Power BI

O projeto foi estruturado com foco em boas práticas de engenharia, reprodutibilidade e manutenibilidade.

2. Arquitetura do Pipeline
             +------------------------------+
             |      Geração de Dados        |
             |        (Python / Pandas)     |
             +--------------+---------------+
                            |
                            v
             +------------------------------+
             |      Armazenamento           |
             |      SQLite (Modelo Estrela) |
             +--------------+---------------+
                            |
                            v
             +------------------------------+
             | Transformações & Métricas    |
             |       (Pandas + SQL)         |
             +--------------+---------------+
                            |
                            v
             +------------------------------+
             |     Exportação / Automação   |
             |   Scripts Python (CSV / DB)  |
             +--------------+---------------+
                            |
                            v
             +------------------------------+
             |   Camada de Visualização     |
             |         Power BI             |
             +------------------------------+


A arquitetura foi desenhada para ser simples, reprodutível e compatível com ferramentas de BI utilizadas no mercado.

3. Modelo de Dados (Data Warehouse)

O armazenamento segue um modelo estrela, composto por:

Tabela Fato

fato_vendas

Grão: 1 linha = 1 venda registrada

Campos principais: id_venda, id_cliente, id_produto, quantidade, valor_total, data_venda

Tabelas Dimensão

dim_clientes

dim_produtos

dim_calendario

Tabelas Auxiliares

metas_kpi

tabela_medidas

atualizacao

4. Decisões Técnicas
SQLite como fonte de dados

leve

fácil de integrar

excelente para prototipação

relacional e estruturado

Estrutura modular

notebooks → exploração e desenvolvimento

scripts → automação

data/ → outputs rastreáveis

dashboard/ → camada de BI

Uso de dados sintéticos

sem restrições de privacidade

permite controle total da lógica

possibilita cenários de teste realistas

Pipeline automatizado

Simula rotinas recorrentes como:

ingestão

enriquecimento

atualização

exportação

5. Etapas do Pipeline
1) Geração e Carga (Python + SQLite)

criação do banco

simulação das tabelas

inserção dos registros

validação

2) Transformações (Pandas + SQL)

limpeza

consolidação

métricas de negócio

exportação para CSV

3) Automação

Script principal:

scripts/automacao_ecommerce.py

4) Visualização (Power BI)

Indicadores:

faturamento

ticket médio

categorias

metas

atualização automática

6. Principais Insights

Eletrônicos: maior impacto em receita

Eletrônicos + Alimentos: maior giro

Ticket médio estável e crescente

Metas e atualização garantem governança

7. Tecnologias Utilizadas
Tecnologia	Finalidade
Python 3.11	Geração e automação
Pandas / NumPy	Manipulação e análise
SQLite3	Armazenamento relacional
Power BI	Visualização
Git & GitHub	Versionamento
8. Estrutura do Repositório
ecommerce-data-analytics_Gustavo_Paula_Silva/
│
├── dashboard/          # Power BI (.pbix)
├── data/               # Banco SQLite e CSVs exportados
├── imagens/            # Screenshots e diagramas
├── notebooks/          # Notebooks Jupyter
├── scripts/            # Automação Python
│
├── .gitignore
├── README.md
└── requirements.txt

9. Como Executar
# 1. Clone o repositório
git clone https://github.com/gustavogit4/ecommerce-data-analytics.git

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a automação
python scripts/automacao_ecommerce.py

# 4. Abra o dashboard no Power BI
dashboard/ecommerce_dashboard.pbix

10. Limitações

dados sintéticos não refletem sazonalidade real

ausência de logs estruturados

não há testes automatizados

SQLite não suporta alta concorrência

11. Possíveis Melhorias

migração para PostgreSQL / DuckDB

criação de logs com logging

DAG no Airflow

containerização (Docker)

calendário analítico dedicado

12. Contato

Gustavo de Paula Silva
Analista de Dados
Pós-graduação em Estatística para Ciência de Dados — PUC Minas

📧 gdepaulasilva966@gmail.com

🐙 GitHub: @gustavogit4



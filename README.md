# E-commerce Data Analytics — Gustavo de Paula Silva  

Simulação completa de um ambiente de **análise e automação de dados**, integrando Python, SQLite e Power BI.

---

## Objetivo

O projeto tem como objetivo representar o ciclo real de trabalho de um **Analista de Dados**, desde a geração até a visualização e automação das informações.  

Foi desenvolvido um **e-commerce fictício**, com dados sintéticos realistas que simulam o comportamento de clientes, produtos e vendas.

---

## Etapas do Projeto

### 1️⃣ Geração e Carga de Dados (Python + SQLite)
- Criação do banco de dados relacional `ecommerce_realista.db`.
- Tabelas: **clientes**, **produtos** e **vendas**.
- Simulação de dados coerentes com o contexto de um e-commerce real.

### 2️⃣ Transformação e Análise de Dados (Pandas + SQL)
- Limpeza, transformação e consolidação das tabelas.
- Cálculo de métricas de desempenho: faturamento, ticket médio, vendas por categoria e cliente.
- Armazenamento dos resultados em `data_export/`.

### 3️⃣ Automação de Processos (Python Script)
- Geração automática de relatórios CSV e atualização do banco SQLite.
- Script: `scripts/automacao_ecommerce.py`
- Execução automatizada do pipeline de dados.

### 4️⃣ Dashboard Interativo (Power BI)
- Criação de dashboard com KPIs, filtros e indicadores visuais.
- Conexão direta com o banco SQLite e arquivos CSV exportados.
- Indicadores: **Faturamento Total**, **Ticket Médio**, **Metas**, **Atualização Automática**.

---

## 📊 Dashboard

### Power BI — *E-commerce Data Analytics*
![Dashboard Preview](dashboard/dashboard_preview.png)

O arquivo do dashboard está disponível em:  
📁 `dashboard/ecommerce_dashboard.pbix`

---

## Modelo de Dados

![Modelo de Dados](dashboard/dashboard_model.png)

Esquema estrela com a tabela fato `vendas` e dimensões `clientes`, `produtos`, `metas_kpi`, `tabela_medidas` e `atualizacao`.

---

## Principais Insights

- A categoria **Eletrônicos** possui o **maior faturamento** e garante estabilidade financeira.  
- **Eletrônicos** e **Alimentos** representam categorias de alto giro.  
- O **ticket médio** se mantém estável, com tendência de crescimento nos últimos meses.  
- O painel possui **metas dinâmicas**, permitindo avaliar o desempenho em tempo real.

---

## Tecnologias Utilizadas

| Tecnologia | Descrição |
|-------------|------------|
| **Python 3.11** | Geração e automação de dados |
| **Pandas / Numpy** | Manipulação e análise |
| **SQLite3** | Armazenamento relacional |
| **Power BI** | Visualização e KPIs |
| **Git & GitHub** | Controle de versão |

---

## Estrutura do Projeto

```text
ecommerce-data-analytics_Gustavo_Paula_Silva/
│
├── dashboard/          # Arquivos do Power BI
├── data/               # Banco de dados e dados exportados
├── imagens/            # Recursos visuais (screenshots, capas, etc.)
├── notebooks/          # Notebooks Jupyter
├── scripts/            # Código Python de automação
│
├── .gitignore
├── README.md
└── requirements.txt

---

## 🔄 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/gustavogit4/ecommerce-data-analytics.git

2. Instale as dependências:
   pip install -r requirements.txt

3. Execute o script de automação:
   python scripts/automacao_ecommerce.py

4. Abra o dashboard no Power BI:
   dashboard/ecommerce_dashboard.pbix

---

Autor
Gustavo de Paula Silva
Analista de Dados | Pós-graduação em Estatística para Ciência de Dados — PUC Minas
E-mail: gdepaulasilva966@gmail.com
GitHub: @gustavogit4

---

Status:

Projeto concluído — versão final publicada no GitHub.
Última atualização: outubro/2025

---





# Análise e Automação de Vendas de um E-commerce Brasileiro

Este projeto simula um ambiente completo de **análise e automação de dados** para um e-commerce fictício, desenvolvido em **Python**, **SQL** e **Power BI**.

O objetivo é demonstrar, de forma prática e realista, o ciclo completo de trabalho de um Analista de Dados — da criação do banco relacional à geração automatizada de relatórios e dashboards.

## Objetivo do Projeto

O projeto tem como objetivo construir um **pipeline de dados completo**, cobrindo todas as etapas do ciclo analítico:

1. **Geração e modelagem dos dados** — criação de um banco relacional com dados sintéticos realistas.  
2. **Transformação e análise exploratória** — integração de consultas SQL e manipulação com Pandas.  
3. **Automação do processo** — exportação automática de relatórios e logs.  
4. **Integração com Business Intelligence (BI)** — visualização e acompanhamento de KPIs no Power BI.

Esse fluxo representa o processo real de um analista de dados corporativo:  
coleta, limpeza, análise, visualização e automação de insights.

## Estrutura do Projeto

```text
ecommerce-data-analytics/
│
├── data/                            → Banco de dados relacional (SQLite)
│   ├── ecommerce_realista.db        → Base principal de dados
│   └── data_export/                 → Relatórios e exportações automáticas (.csv)
│
├── imagens/                         → Gráficos gerados nas análises exploratórias
│   ├── faturamento_canais.png
│   ├── faturamento_categorias.png
│   ├── produtos_mais_vendidos.png
│   ├── produtos_maior_faturamento.png
│   ├── clientes_top10.png
│   └── clientes_pareto.png
│
├── notebooks/                       → Notebooks Jupyter com as etapas do pipeline
│   ├── 01_geracao_dados.ipynb       → Etapa 1 — geração e modelagem de dados
│   ├── 02_transformacao_analise_ecommerce.ipynb  → Etapa 2 — exploração e análise
│   └── 03_automacao_ecommerce.ipynb → Etapa 3 — automação e integração com Power BI
│
├── scripts/                         → Scripts Python independentes
│   └── automacao_ecommerce.py       → Script principal de automação modular
│
├── requirements.txt                 → Lista de dependências do projeto
├── .gitignore                       → Arquivos e pastas ignorados no versionamento
└── README.md                        → Documentação completa do projeto


```

## Tecnologias Utilizadas

- **Linguagem:** Python  
- **Bibliotecas:** **Pandas**, **NumPy**, **Faker**, **Matplotlib**, **Seaborn**  
- **Banco de Dados:** SQLite  
- **Visualização e Business Intelligence:** Power BI  
- **Ambiente de Desenvolvimento:** VS Code  
- **Controle de Versão:** Git e GitHub

## Etapas do Projeto

O projeto adota uma arquitetura de **pipeline ELT (Extract, Load, Transform)**, desenvolvida em Python e integrada a um banco de dados relacional SQLite.

Cada etapa representa uma fase do processo analítico — da criação dos dados até a automação e integração com Business Intelligence.

### 01 - Geração e Carga de Dados (E + L)
Criação de dados sintéticos realistas utilizando **Faker** e **NumPy**, seguidos da carga automatizada no banco `ecommerce_realista.db`.

**Status:** Concluído ✅

---

### 02 - Transformação e Análise (T)
Integração de consultas **SQL** e manipulações com **Pandas**, permitindo compreender o comportamento de compra dos clientes, o desempenho das categorias e o equilíbrio entre os canais de venda.

**Principais indicadores:**
- Faturamento total: R$ 5,87 milhões  
- Ticket médio: R$ 210,50  
- Canais equilibrados entre loja física e e-commerce  
- Efeito Pareto (20% dos clientes → 80% da receita)

**Status:** Concluído ✅

---

### 03 - Automação e Power BI
Automação completa da extração, transformação e exportação dos relatórios, com versionamento automático por data e registro de logs.

Integração planejada com **Power BI** para criação de dashboards interativos e acompanhamento de KPIs em tempo real.

**Status:** Em andamento 🔄

## Execução Local

### Requisitos

- **Python:** Versão 3.10 ou superior  
- **Dependências:** Listadas no arquivo `requirements.txt`

---

### Instalação

No terminal, dentro da pasta do projeto:

```bash
pip install -r requirements.txt

Execução:

Após a instalação, execute o script principal:
python automacao_ecommerce.py

Saída esperada no terminal:
Iniciando automação de dados...
Processo concluído com sucesso! Ticket médio: R$ 392.42

Os arquivos CSV e logs serão gerados automaticamente na pasta:
data_export/
├── vendas_detalhadas_YYYY-MM-DD.csv
├── resumo_categorias_YYYY-MM-DD.csv
├── resumo_clientes_YYYY-MM-DD.csv
└── log_execucao.txt

Execução via Notebook:

Também é possível rodar o processo dentro do Jupyter Notebook:
notebooks/03_automacao_ecommerce.ipynb
Basta executar todas as células na sequência.
```
## Autor

**Gustavo de Paula Silva**  
Analista de Dados | Pós-graduação em Estatística para Ciência de Dados — PUC Minas  
E-mail: gdepaulasilva966@gmail.com  
GitHub: [@gustavogit4](https://github.com/gustavogit4)

---

## Versão

**Versão atual:** 1.1.0 — Automação modular com docstrings e logging estruturado  
**Última atualização:** 26/10/2025
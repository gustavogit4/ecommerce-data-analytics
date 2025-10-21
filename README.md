📊 Etapas do Projeto
O projeto segue uma arquitetura de pipeline ELT (Extract, Load, Transform), desenvolvida em Python e integrada ao banco relacional SQLite.  

As análises foram divididas em etapas modulares, cada uma representando uma fase real do trabalho de um Analista de Dados:

| Etapa | Descrição | Status |
|-------|------------|--------|
| 🧱 **01 - Geração e Carga de Dados (E + L)** | Geração de dados sintéticos com Faker e NumPy e carga automatizada no banco `ecommerce_realista.db`. | ✅ Concluído |
| 🧮 **02 - Transformação e Análise (T)** | Aplicação de transformações analíticas em SQL e Python para criação de métricas e visualizações estratégicas. | ✅ Concluído |
| ⚙️ **03 - Automação e Power BI** | Integração e criação de dashboard dinâmico com atualização automática. | 🔜 Próxima etapa |

---

## 📈 Etapa 2 — Transformação e Análise

Nesta fase, os dados foram tratados e analisados para compreender o comportamento de compra dos clientes, o desempenho das categorias e o equilíbrio entre os canais de venda.  

As consultas SQL foram integradas ao Python para gerar **indicadores de faturamento, ticket médio e volume de vendas**, visualizados por meio de gráficos.

---

### 🔹 Principais Resultados

#### Faturamento por Categoria
![Faturamento por Categoria](imagens/grafico_categorias.png)

#### Faturamento por Canal de Venda
![Faturamento por Canal](imagens/grafico_canais_venda.png)

#### Top 10 Produtos Mais Vendidos
![Top 10 Produtos](imagens/grafico_produtos_top10.png)

#### Top 10 Clientes por Faturamento
![Top 10 Clientes](imagens/grafico_clientes.png)

#### Curva de Pareto — Distribuição de Faturamento por Cliente
![Pareto Clientes](imagens/grafico_clientes_pareto.png)

---

## 💡 Conclusões e Insights Estratégicos

- **Faturamento total:** R$ 5,87 milhões, com 27 mil produtos vendidos e ticket médio de R$ 210,50.  
- **Canais equilibrados:** E-commerce e loja física dividiram o faturamento de forma equilibrada (~R$ 2,56 milhões cada), demonstrando uma operação omnichannel madura.  
- **Categoria dominante:** Eletrônicos concentraram 86% da receita, com ticket médio de R$ 1.659, reforçando o peso dos produtos premium.  
- **Comportamento de clientes:** Um pequeno grupo de clientes gerou a maior parte das receitas, confirmando o **efeito Pareto (80/20)**.  
- **Base de dados consistente:** Após limpeza e validações, não foram encontradas duplicatas e apenas nulos esperados em campos de canal de venda.  

🔎 *Síntese:*  
A operação do e-commerce é eficiente e concentrada em clientes e produtos de alto valor.  
As próximas etapas focarão na **automação e visualização dos KPIs no Power BI**, integrando as métricas de receita, canal e cliente em dashboards dinâmicos.

---

## 🧠 Tecnologias Utilizadas
- **Python** → Pandas, NumPy, Matplotlib, Seaborn, SQLite3  
- **Banco de Dados** → SQLite  
- **Visualização e BI** → Power BI (próxima etapa)  
- **Controle de Versão** → Git & GitHub  

---

## 🧩 Estrutura do Repositório
├── data/
│ └── ecommerce_realista.db
├── imagens/
│ ├── grafico_categorias.png
│ ├── grafico_canais_venda.png
│ ├── grafico_produtos_top10.png
│ ├── grafico_clientes.png
│ ├── grafico_clientes_pareto.png
│ └── grafico_faturamento_total.png
├── notebooks/
│ ├── 01_geracao_dados.ipynb
│ └── 02_transformacao_analise_ecommerce.ipynb
└── README.md

## 🗃️ Estrutura do Banco de Dados

**Arquivo:** `data/ecommerce_realista.db`

O banco de dados foi construído em **SQLite**, adotando um **modelo estrela (Star Schema) simplificado**, amplamente utilizado em projetos de **Business Intelligence** e **Data Warehousing**.

Nesse modelo, as **tabelas dimensão** armazenam informações descritivas (como clientes e produtos), enquanto a **tabela fato** centraliza os eventos de negócio — neste caso, as vendas.

---

### 🔹 Modelo de Dados

#### **1. Dimensão: Clientes**
Armazena informações demográficas e cadastrais dos clientes.  
Campos principais:
- `id_cliente` (PRIMARY KEY)  
- `nome`  
- `idade`  
- `genero`  
- `cidade`  
- `estado`  
- `data_cadastro`

#### **2. Dimensão: Produtos**
Contém informações sobre os produtos disponíveis no e-commerce.  
Campos principais:
- `id_produto` (PRIMARY KEY)  
- `categoria`  
- `preco`  
- `descricao`

#### **3. Fato: Vendas**
Registra cada transação realizada por um cliente.  
Campos principais:
- `id_venda` (PRIMARY KEY)  
- `id_cliente` (FOREIGN KEY → clientes)  
- `id_produto` (FOREIGN KEY → produtos)  
- `quantidade`  
- `data_venda`  
- `canal_venda`  
- `valor_total`

---

### 🔹 Relacionamentos

- **1:N** entre **Clientes → Vendas**  
  (um cliente pode realizar várias compras)  
- **1:N** entre **Produtos → Vendas**  
  (um produto pode estar presente em várias transações)

Essa estrutura permite análises de negócio como:
- Total de vendas por **canal**, **estado** ou **faixa etária**  
- Ticket médio e valor total gasto por **cliente**  
- Faturamento por **categoria de produto**  
- Tendências de vendas ao longo do **tempo**

---

> O banco pode ser consultado via Python (`sqlite3` ou `pandas.read_sql_query`) ou conectado diretamente ao **Power BI**, preservando os relacionamentos originais para criação de dashboards analíticos.

---

## 🧠 Autor

**👤 Gustavo de Paula Silva**  
📍 Analista de Dados  
📧 gdepaulasilva966@gmail.com  
🔗 [GitHub @gustavogit4](https://github.com/gustavogit4)  

---

> 💡 *Este projeto integra práticas reais de Data Analytics e Business Intelligence, com foco em aprendizado contínuo e aplicação prática em cenários de negócio.*


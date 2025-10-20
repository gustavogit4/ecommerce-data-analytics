# 🛒 Análise e Automação de Vendas de um E-commerce Brasileiro

Este projeto simula um ambiente completo de **análise e automação de dados** para um e-commerce fictício,
com foco em demonstrar habilidades práticas em **Python, SQL e Power BI** aplicadas à tomada de decisão.

---

## 🎯 Objetivo do Projeto

Construir um **pipeline de dados completo** — da geração e modelagem até a análise e automação de relatórios —  
representando o ciclo real de trabalho de um **Analista de Dados** em um ambiente corporativo.

---

## 🧠 Estrutura do Projeto

| Diretório / Arquivo | Descrição |
|----------------------|------------|
| 📁 `data/` | Contém o banco de dados relacional `ecommerce_realista.db` |
| 📁 `notebooks/` | Códigos em Python (.ipynb) para geração, exploração e análise dos dados |
| 📄 `README.md` | Documentação completa do projeto |
| ⚙️ `requirements.txt` | Lista de dependências utilizadas |

---

## 🧩 Tecnologias Utilizadas

- **Python** → Pandas, NumPy, Faker, Matplotlib, Seaborn  
- **Banco de Dados** → SQLite  
- **Visualização e BI** → Power BI  
- **Controle de Versão** → Git & GitHub  

---

## 📊 Etapas do Projeto

O projeto segue uma arquitetura de **pipeline ELT (Extract, Load, Transform)**, desenvolvida em **Python** e integrada ao banco relacional **SQLite**.

Nesta etapa inicial, o foco está na **geração e carga dos dados** no banco, simulando um processo real de ingestão e armazenamento de dados corporativos.

| Etapa | Descrição | Status |
|-------|------------|--------|
| 🧱 **01 - Geração e Carga de Dados (E + L)** | Geração de dados sintéticos com Faker e NumPy e carga automatizada no banco `ecommerce_realista.db`. | ✅ Concluído |
| 🧮 **02 - Transformação e Análise (T)** | Aplicação de transformações analíticas em SQL e Python para criação de métricas e visualizações. | 🚧 Em desenvolvimento |
| ⚙️ **03 - Automação e Power BI** | Integração e criação de dashboard dinâmico com atualização automática. | 🔜 Próxima etapa |

> 💡 O projeto implementa um pipeline **ELT**, prática comum em arquiteturas modernas de dados:  
> - **Extract** → Geração de dados sintéticos  
> - **Load** → Carga no banco SQLite  
> - **Transform** → Consultas SQL e análises em Python e Power BI

---

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

import os
import pandas as pd
import sqlite3
from datetime import datetime

# ===============================================================
# 1️⃣ Configurações Iniciais
# ===============================================================
DB_PATH = r'C:\Users\--\Desktop\ecommerce-data-analytics\data\ecommerce_realista.db'
EXPORT_PATH = r'C:\Users\--\Desktop\ecommerce-data-analytics\data\data_export'
os.makedirs(EXPORT_PATH, exist_ok=True)

# ===============================================================
# 2️⃣ Conexão e Leitura das Tabelas
# ===============================================================
with sqlite3.connect(DB_PATH) as conn:
    clientes = pd.read_sql("SELECT * FROM clientes", conn)
    produtos = pd.read_sql("SELECT * FROM produtos", conn)
    vendas = pd.read_sql("SELECT * FROM vendas", conn)

print("✅ Tabelas carregadas com sucesso.")

# ===============================================================
# 3️⃣ Transformações e Cálculos
# ===============================================================
df = vendas.merge(produtos, on='id_produto', how='left')
df = df.merge(clientes, on='id_cliente', how='left')

df['valor_total_calc'] = df['quantidade'] * df['preco_unitario']
ticket_medio = df['valor_total_calc'].mean()
print(f"💰 Ticket médio: R$ {ticket_medio:.2f}\n")

# ===============================================================
# 4️⃣ Exportação dos Resultados
# ===============================================================
data_hoje = datetime.now().strftime('%Y-%m-%d')

df.to_csv(f'{EXPORT_PATH}/vendas_detalhadas_{data_hoje}.csv', index=False, encoding='utf-8')
resumo_cat = df.groupby('categoria')['valor_total_calc'].sum().reset_index()
resumo_cat.to_csv(f'{EXPORT_PATH}/resumo_categorias_{data_hoje}.csv', index=False, encoding='utf-8')
resumo_cli = df.groupby('nome')['valor_total_calc'].sum().reset_index()
resumo_cli.to_csv(f'{EXPORT_PATH}/resumo_clientes_{data_hoje}.csv', index=False, encoding='utf-8')

print("📦 Arquivos exportados com sucesso!")

# ===============================================================
# 5️⃣ Log de Execução
# ===============================================================
with open(f'{EXPORT_PATH}/log_execucao.txt', 'a') as log:
    log.write(f'Atualização realizada em {data_hoje}\n')

print("🕒 Log de execução atualizado.")
print("🚀 Processo de automação concluído com sucesso!")

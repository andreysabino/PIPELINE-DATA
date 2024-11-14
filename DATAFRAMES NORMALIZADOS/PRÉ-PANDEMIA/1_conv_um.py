import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('PP.csv')

# Remover aspas e substituir vírgulas por pontos em todas as colunas
df = df.replace('"', '', regex=True)
df = df.replace(',', '.', regex=True)

# Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv('PP-V1.csv', index=False)

print("Conversão concluída. Arquivo salvo como 'PRÉ_PANDEMIA-V1.csv'")

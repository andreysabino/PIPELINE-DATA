import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('PP-V1.csv')

# Converter as colunas 'MEDIA' e 'PE' para float
df['PE'] = df['PE'].astype(float)

# Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv('PP-VF.csv', index=False)

print("Conversão concluída. Arquivo salvo como 'PP-VF.csv'")

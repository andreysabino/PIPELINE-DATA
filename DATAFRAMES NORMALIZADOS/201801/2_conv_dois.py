import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('201801_converted.csv')

# Converter as colunas 'MEDIA' e 'PE' para float
df['MEDIA'] = df['MEDIA'].astype(float)
df['PE'] = df['PE'].astype(float)

# Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv('TCC201801_converted.csv', index=False)

print("Conversão concluída. Arquivo salvo como 'TCC201801_converted_final.csv'")

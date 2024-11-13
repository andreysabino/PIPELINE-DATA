import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('201902-RV1.csv')

# Converter as colunas 'MEDIA' e 'PE' para float
df['PE'] = df['PE'].astype(float)

# Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv('201902 - RVF.csv', index=False)

print("Conversão concluída. Arquivo salvo como '201902-VF.csv'")

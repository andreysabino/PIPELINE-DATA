import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('"201802-VF.csv"')

# Converter as colunas 'MEDIA' e 'PE' para float
df['MEDIA'] = df['MEDIA'].astype(float)
df['PE'] = df['PE'].astype(float)

# Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv('201802-VF', index=False)

print("Conversão concluída. Arquivo salvo como 'TCC201801_converted_final.csv'")

import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('201901-C.csv')

# Remover aspas na coluna 'PE', substituir vírgulas por pontos e remover caracteres indesejados
df['PE'] = df['PE'].str.replace('"', '').str.replace(',', '.').str.replace(r'[^0-9.]', '', regex=True).astype(float)

# Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv('201901-VF.csv', index=False)

print("Conversão concluída. Arquivo salvo como '201901-V1.csv'")
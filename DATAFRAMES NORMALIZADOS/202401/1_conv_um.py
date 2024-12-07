import pandas as pd

# Leia o arquivo CSV
df = pd.read_csv('202401.csv')

# Remova as aspas e substitua as vírgulas por pontos nas colunas 'MEDIA' e 'PE'
df['MEDIA'] = df['MEDIA'].str.replace('"', '').str.replace(',', '.')
df['PE'] = df['PE'].str.replace('"', '').str.replace(',', '.')

# Salve o arquivo CSV atualizado
df.to_csv('202401-V1-updated.csv', index=False)
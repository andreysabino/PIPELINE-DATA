import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('DFC.csv')

# Iterar sobre os valores da coluna 'PE' e imprimir o tipo de cada valor
for value in df['PE']:
    print(f"Valor: {value}, Tipo: {type(value)}")

for value in df['MEDIA']:
    print(f"Valor: {value}, Tipo: {type(value)}")

for value in df['ID']:
    print(f"Valor: {value}, Tipo: {type(value)}")
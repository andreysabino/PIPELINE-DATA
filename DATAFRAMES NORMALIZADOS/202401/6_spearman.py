import pandas as pd
from scipy.stats import spearmanr

# Carregar o DataFrame a partir de um arquivo CSV (substitua 'seu_arquivo.csv' pelo nome do seu arquivo)
df = pd.read_csv('202401-VF.csv')

# Calcular o coeficiente de Spearman entre as colunas 'PE' e 'MEDIA'
spearman_corr, p_value = spearmanr(df['PE'], df['MEDIA'])

# Exibir o resultado
print(f"Coeficiente de Spearman: {spearman_corr}")
print(f"Valor-p: {p_value}")

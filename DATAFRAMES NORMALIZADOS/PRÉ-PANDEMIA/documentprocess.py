import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pearsonr

# Diretório base
base_dir = 'C:/Users/andre/OneDrive/Área de Trabalho/TCC/PIPELINE-DATA/DATAFRAMES NORMALIZADOS/PRÉ-PANDEMIA'

# Criar subpastas
os.makedirs(f'{base_dir}/graficos', exist_ok=True)

# Carregar o DataFrame
df = pd.read_csv(f'{base_dir}/POSP.csv')

# Calcular coeficientes de Spearman e Pearson
spearman_corr, spearman_p = spearmanr(df['PE'], df['MEDIA'])
pearson_corr, pearson_p = pearsonr(df['PE'], df['MEDIA'])

# Gerar gráfico de dispersão
plt.figure()
plt.scatter(df['PE'], df['MEDIA'])
plt.title('Gráfico de Dispersão')
plt.xlabel('PE')
plt.ylabel('MEDIA')
plt.savefig(f'{base_dir}/graficos/dispersao.png')

# Gerar boxplot para 'PE'
plt.figure()
df.boxplot(column=['PE'])
plt.title('Boxplot de PE')
plt.savefig(f'{base_dir}/graficos/boxplot_pe.png')

# Gerar boxplot para 'MEDIA'
plt.figure()
df.boxplot(column=['MEDIA'])
plt.title('Boxplot de MEDIA')
plt.savefig(f'{base_dir}/graficos/boxplot_media.png')

# Criar arquivo Markdown com os resultados
with open(f'{base_dir}/Readme.md', 'w') as f:
    f.write("# Resultados de Análise\n")
    f.write("## Coeficientes de Correlação\n")
    f.write(f"### Spearman\n")
    f.write(f"- Coeficiente de Spearman: {spearman_corr}\n")
    f.write(f"- Valor-p: {spearman_p}\n")
    f.write(f"### Pearson\n")
    f.write(f"- Coeficiente de Pearson: {pearson_corr}\n")
    f.write(f"- Valor-p: {pearson_p}\n")
    f.write("\n## Gráficos\n")
    f.write("### Gráfico de Dispersão\n")
    f.write(f"![Gráfico de Dispersão](graficos/dispersao.png)\n")
    f.write("### Boxplot de PE\n")
    f.write(f"![Boxplot de PE](graficos/boxplot_pe.png)\n")
    f.write("### Boxplot de MEDIA\n")
    f.write(f"![Boxplot de MEDIA](graficos/boxplot_media.png)\n")
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para plotar gráficos

# Carregar os dados do CSV
df = pd.read_csv("202201-VF.csv")  # Lê o arquivo CSV e armazena os dados em um DataFrame

# Criar um gráfico de dispersão
plt.scatter(df['PE'], df['MEDIA'])  # Cria um gráfico de dispersão com 'PE' no eixo X e 'MEDIA' no eixo Y
plt.xlabel('PE')  # Adiciona o rótulo do eixo X
plt.ylabel('MEDIA')  # Adiciona o rótulo do eixo Y
plt.title('CORRELATION - MEDIA AND PE (2019.01)')  # Adiciona o título do gráfico
plt.show()  # Exibe o gráfico
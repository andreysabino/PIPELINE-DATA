import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para plotar gráficos

# Carregar os dados do CSV
df = pd.read_csv("201901-VF.csv")  # Lê o arquivo CSV e armazena os dados em um DataFrame

# Calcular a correlação de Pearson entre as colunas 'MEDIA' e 'PE'
correlation = df['MEDIA'].corr(df['PE'])  # Calcula o coeficiente de correlação de Pearson
print("Correlação de Pearson:", correlation)  # Imprime o coeficiente de correlação de Pearson

# Grafico de dispersãoD
plt.scatter(df['MEDIA'], df['PE'])  # Cria um gráfico de dispersão com 'MEDIA' no eixo X e 'PE' no eixo Y
plt.xlabel('Média em Algoritmos')  # Adiciona o rótulo do eixo X
plt.ylabel('Porcentagem de Frequência')  # Adiciona o rótulo do eixo Y
plt.title('Relação entre Média em Algoritmos e Frequência (2019.02)')  # Adiciona o título do gráfico
plt.show()  # Exibe o gráfico

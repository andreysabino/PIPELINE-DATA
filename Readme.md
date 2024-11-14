# Documentação do Processo de Análise de Dados

**Autor:** Andrey de Oliveira Sabino

**Orientador:** Prof. Dr. Alysson Filgueira Milanez

**Finalidade:** Este projeto de pesquisa tem como objetivo contribuir para o ensino de programação por meio da análise de dados sobre frequência e desempenho dos alunos. Busca-se avaliar os impactos das ações de extensão na aprendizagem e na eficiência dos estudantes nas disciplinas introdutórias de programação. Especificamente, esta pesquisa foca em analisar como a ação de ensino "Pré-Algoritmos" influencia o rendimento acadêmico dos alunos na disciplina de Algoritmos e Programação.

## Organização do Diretório

Os dados e scripts estão organizados da seguinte forma:

```
DATAFRAMES/
├── 201801/
│   ├── 1_conversao_inicial.py
│   ├── 2_conversao_secundaria.py
│   ├── 3_type.py
│   ├── 4_PEAR.py
│   ├── 5_DISP.py
│   ├── 2001801-VF.csv
│   ├── Readme.md
├── 201802/
│   ├── 1_conversao_inicial.py
│   ├── 2_conversao_secundaria.py
│   ├── 3_type.py
│   ├── 4_PEAR.py
│   ├── 5_DISP.py
│   ├── 201802-VF.csv
│   ├── Readme.md
├── 201901/
│   ├── 1_conversao_inicial.py
│   ├── 2_conversao_secundaria.py
│   ├── 3_type.py
│   ├── 4_PEAR.py
│   ├── 5_DISP.py
│   ├── 201901-VF.csv
│   ├── Readme.md
├── 201902/
│   ├── 1_conversao_inicial.py
│   ├── 2_conversao_secundaria.py
│   ├── 3_type.py
│   ├── 4_PEAR.py
│   ├── 5_DISP.py
│   ├── 201902-VF.csv
│   ├── Readme.md
├── 202201/
│   ├── 1_conversao_inicial.py
│   ├── 2_conversao_secundaria.py
│   ├── 3_type.py
│   ├── 4_PEAR.py
│   ├── 5_DISP.py
│   ├── 202001-VF.csv
│   ├── Readme.md
```

Cada pasta dentro do diretório `DATAFRAMES` corresponde a um semestre e contém os arquivos CSV resultantes de cada etapa do processo (conversão, limpeza e normalização), bem como os scripts utilizados para cada etapa.

- [`1_conversao_inicial.py`](#script-de-conversão-inicial): Script para a conversão inicial dos dados.
- [`2_conversao_secundaria.py`](#script-de-conversão-secundária): Script para a segunda fase de conversão dos dados.
- [`3_type.py`](#script-de-verificação-de-tipos): Script para verificar os tipos de dados.
- [`4_PEAR.py`](#script-para-calcular-o-coeficiente-de-pearson): Script para calcular o coeficiente de correlação de Pearson.
- [`5_DISP.py`](#script-para-geraçã-de-gráficos-de-dispersão): Script para gerar gráficos de dispersão.
- [`2001801-VF.csv`](#dados-convertidos): Arquivo CSV resultante da conversão inicial dos dados.
- [`Readme.md`]:() Arquivo .MD com os insights dos datos de seu devido diretório.


## Padrão de Commits

Para manter um histórico de commits claro e consistente, segui o seguinte padrão de commits:

- **feat**: Adiciona uma nova funcionalidade.
- **fix**: Corrige um bug.
- **docs**: Altera a documentação.
- **style**: Alterações de estilo (espaçamento, formatação, etc.).
- **refactor**: Melhora o código sem alterar a funcionalidade.
- **test**: Adiciona ou modifica testes.
- **chore**: Alterações que não afetam o código ou os testes (ex: configuração de build).

## Bibliotecas Utilizadas

### Pandas

[Pandas](https://pandas.pydata.org/) é uma biblioteca poderosa e flexível para manipulação e análise de dados. Ela fornece estruturas de dados de alto desempenho e fáceis de usar, como DataFrames, que são essenciais para a análise de dados.

### Matplotlib

[Matplotlib](https://matplotlib.org/) é uma biblioteca de plotagem em 2D que permite criar gráficos e visualizações de dados de forma simples e intuitiva. É amplamente utilizada para gerar gráficos de dispersão, histogramas, gráficos de linha, entre outros.

### Scipy

[Scipy](https://www.scipy.org/) é uma biblioteca que fornece rotinas e algoritmos científicos e técnicos. No contexto deste projeto, utilizamos o módulo `scipy.stats` para calcular o coeficiente de correlação de Spearman.

### Seaborn

[Seaborn](https://seaborn.pydata.org/) é uma biblioteca de visualização de dados baseada no Matplotlib. Ela fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos.

### Tabula

[Tabula](https://tabula.technology/) é uma ferramenta para extrair tabelas de arquivos PDF. Utilizamos a biblioteca `tabula-py` para converter os dados dos arquivos PDF para formatos manipuláveis como `.xlsx` e `.csv`.

## 1. Introdução

Este documento detalha o processo de análise de dados realizado no projeto de TCC, desde a conversão dos dados originais em formato `.pdf` para `.xlsx` e `.csv`, até a limpeza, normalização e preparação dos dados para a análise final. O objetivo é explicar o passo a passo seguido e os desafios enfrentados ao longo do processo.

## 2. Conversão dos Arquivos PDF para XLSX/CSV

Os dados originais estavam em arquivos PDF, o que dificultava a manipulação direta dos mesmos. Para converter esses arquivos em formatos que permitissem uma análise mais flexível, utilizei o script Python abaixo:

```python
import tabula
import pandas as pd
from google.colab import files

# Carregar o arquivo PDF
uploaded = files.upload()
pdf_file = list(uploaded.keys())[0]

# Extrair todas as tabelas do PDF
tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True, guess=True, stream=True)

# Salvar cada tabela como um arquivo Excel e CSV
for i, tabela in enumerate(tables):
  xlsx_file = f"tabela_{i+1}.xlsx"
  csv_file = f"tabela_{i+1}.csv"
  tabela.to_excel(xlsx_file, index=False)
  tabela.to_csv(csv_file, index=False)
  print(f"Tabela {i+1} salva como {xlsx_file} e {csv_file}")
  files.download(xlsx_file)
  files.download(csv_file)
```

## 3. Limpeza e Redução de Colunas

Após a conversão dos arquivos PDF para formatos manipuláveis como `.xlsx` e `.csv`, iniciou-se a fase de limpeza dos dados. Esta fase incluiu a remoção de colunas irrelevantes, tratamento de dados ausentes e padronização de formatos.

### Fase Inicial de Limpeza

1. **Remoção de Colunas Irrelevantes**: Muitas colunas presentes nos dados originais não eram necessárias para a análise. Essas colunas foram removidas para simplificar o conjunto de dados.
2. **Tratamento de Dados Ausentes**: Dados ausentes foram identificados e tratados. Dependendo do caso, valores ausentes foram preenchidos com a média da coluna ou removidos.
3. **Padronização de Formatos**: Garantir que todos os dados estavam no formato correto (por exemplo, datas no formato `YYYY-MM-DD`, números como floats ou inteiros conforme necessário).

### Formato dos Dados Antes da Limpeza

Antes da limpeza, os dados tinham o seguinte formato:

| ID  | 06/07/202X | 07/07/202X | 08/07/202X | 09/07/202X | 10/07/202X | 11/07/202X | 12/07/202X | ... |
|-----|------------|------------|------------|------------|------------|------------|------------|-----|
| 1   | V          | F          | V          | V          | V          | V          | F          | ... |
| 2   | V          | V          | F          | F          | V          | V          | V          | ... |

- **V** indica presença, e **F** indica falta.

### Formato dos Dados Após a Limpeza

Após a limpeza, as colunas menos relevantes foram removidas. Como o conjunto de dados se referia à frequência dos alunos, e cada aula gerava uma nova coluna, isso resultava em um excesso de colunas com a presença ou ausência por data.

Para simplificar, optei por representar a frequência dos alunos em forma de porcentagem, indicando a quantidade total de aulas frequentadas. Além disso, incluímos a **média do aluno na disciplina de Algoritmos** e o **status de aprovação**. Com essas alterações, o conjunto de dados ficou assim:

| ID  | Nome do Aluno | Frequência (%) | Média em Algoritmos | Status    |
|-----|---------------|----------------|---------------------|-----------|
| 1   | Aluno A       | 85%            | 7.5                 | Aprovado  |
| 2   | Aluno B       | 75%            | 6.0                 | Aprovado  |
| 3   | Aluno C       | 100%           | 5.0                 | Reprovado |

Essa abordagem oferece uma visão mais resumida e fácil de entender, além de permitir que a análise seja focada não só na frequência, mas também no desempenho dos alunos na disciplina. Dessa forma, ficou mais simples comparar o impacto da frequência no rendimento acadêmico e no status final de aprovação.

### Script de Conversão e Limpeza Inicial

```python
import pandas as pd

# Carregar os dados convertidos
df = pd.read_csv('dados_convertidos.csv')

# Salvar os dados limpos
df.to_csv('dados_limpos.csv', index=False)
```

## 4. Normalização dos Dados

Após a limpeza inicial, foi realizado um processo de normalização para garantir a consistência e facilitar a análise. O processo final resultou em uma tabela com três colunas: `ID`, `MEDIA`, e `PE`.

### Representação da Tabela Final

| ID  | MEDIA | PE   |
|-----|-------|------|
| 1   | 7.5   | 85.0 |
| 2   | 6.0   | 75.0 |
| 3   | 5.0   | 100.0|

- **ID**: Número inteiro identificador do aluno.
- **MEDIA**: Média dos alunos na disciplina de Algoritmos (float).
- **PE**: Percentual na extensão, que é a frequência na extensão (float).

### Scripts Utilizados

#### Script de Conversão Inicial

```python
import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('201802-VF.csv')

# Substituir vírgulas por pontos na coluna 'MEDIA' e remover caracteres indesejados
df['MEDIA'] = df['MEDIA'].str.replace(',', '.').str.replace(r'[^0-9.]', '', regex=True).astype(float)

# Remover aspas na coluna 'PE', substituir vírgulas por pontos e remover caracteres indesejados
df['PE'] = df['PE'].str.replace('"', '').str.replace(',', '.').str.replace(r'[^0-9.]', '', regex=True).astype(float)

# Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv('201802-V1', index=False)

print("Conversão concluída. Arquivo salvo como '201801_converted.csv'")
```

#### Script de Conversão Secundária

```python
import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('"201802-VF.csv"')

# Converter as colunas 'MEDIA' e 'PE' para float
df['MEDIA'] = df['MEDIA'].astype(float)
df['PE'] = df['PE'].astype(float)

# Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv('201802-VF', index=False)

print("Conversão concluída. Arquivo salvo como 'TCC201801_converted_final.csv'")

```

#### Script de Verificação de Tipos

```python
import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('201802-VF.csv')

# Iterar sobre os valores da coluna 'PE' e imprimir o tipo de cada valor
for value in df['PE']:
    print(f"Valor: {value}, Tipo: {type(value)}")

for value in df['MEDIA']:
    print(f"Valor: {value}, Tipo: {type(value)}")

for value in df['ID']:
    print(f"Valor: {value}, Tipo: {type(value)}")
```

#### Script para Calcular o Coeficiente de Pearson

```python
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para plotar gráficos

# Carregar os dados do CSV
df = pd.read_csv("201802-VF.csv")  # Lê o arquivo CSV e armazena os dados em um DataFrame

# Calcular a correlação de Pearson entre as colunas 'MEDIA' e 'PE'
correlation = df['MEDIA'].corr(df['PE'])  # Calcula o coeficiente de correlação de Pearson
print("Correlação de Pearson:", correlation)  # Imprime o coeficiente de correlação de Pearson
```

#### Script para Geração de Gráficos de Dispersão

```python
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para plotar gráficos

# Carregar os dados do CSV
df = pd.read_csv("201802-VF.csv")  # Lê o arquivo CSV e armazena os dados em um DataFrame

# Criar um gráfico de dispersão
plt.scatter(df['PE'], df['MEDIA'])  # Cria um gráfico de dispersão com 'PE' no eixo X e 'MEDIA' no eixo Y
plt.xlabel('Porcentagem de Frequência')  # Adiciona o rótulo do eixo X
plt.ylabel('Média em Algoritmos')  # Adiciona o rótulo do eixo Y
plt.title('CORRELATION - MEDIA AND PE (2018.02)')  # Adiciona o título do gráfico
plt.show()  # Exibe o gráfico
```

## 5. Considerações Sobre a Fase de Limpeza e Normalização

O processo de conversão, limpeza e normalização de dados foi uma etapa crucial para garantir a integridade dos dados utilizados no estudo. Embora tenha havido problemas durante a conversão dos arquivos PDF, todos os erros foram identificados e corrigidos a tempo, garantindo a consistência dos dados.

A partir dos arquivos normalizados, foi possível proceder com a análise de dados, focando nos elementos mais relevantes para os objetivos do TCC.

## 6. Resultados e Conclusões

### Resultados

### 6.1 Semestre 2018.1(<span style="color: blue; font-weight: bold;">Pré-Pandemia</span>)


- **Spearman**: Coeficiente = 0,3873; Valor-p = 0,0124  
- **Pearson**: Coeficiente = 0,5612; Valor-p = 0,0001  

Esses resultados indicam uma correlação positiva moderada entre frequência e desempenho, com significância estatística para ambos os coeficientes. A correlação de Pearson sugere uma relação linear moderada entre frequência e as notas dos alunos.

---

### 6.2 Semestre 2018.2(<span style="color: blue; font-weight: bold;">Pré-Pandemia</span>)


- **Spearman**: Coeficiente = 0,3608; Valor-p = 0,0205  
- **Pearson**: Coeficiente = 0,3606; Valor-p = 0,0206  

A análise deste semestre revela uma correlação positiva moderada e estatisticamente significativa, como sugerido pelos valores-p. Isso indica uma relação entre a frequência nas ações de extensão e o rendimento acadêmico dos alunos.

---

### 6.3 Semestre 2019.1(<span style="color: blue; font-weight: bold;">Pré-Pandemia</span>)


- **Spearman**: Coeficiente = 0,3365; Valor-p = 0,0448  
- **Pearson**: Coeficiente = 0,2904; Valor-p = 0,0858  

Neste semestre, apenas o coeficiente de Spearman apresenta significância estatística, indicando uma correlação monotônica moderada. Já o coeficiente de Pearson não alcançou significância estatística, sugerindo que a relação não é estritamente linear.

---

### 6.4 Semestre 2019.2 (<span style="color: blue; font-weight: bold;">Pré-Pandemia</span>)

- **Spearman**: Coeficiente = 0,3232; Valor-p = 0,0666  
- **Pearson**: Coeficiente = 0,2597; Valor-p = 0,1444  

Neste semestre, ambos os coeficientes não apresentam significância estatística, o que sugere que a relação entre frequência e rendimento pode ser menos pronunciada neste período.

---

### 6.5 Semestre 2022.1 (<span style="color: orange; font-weight: bold;">Pós-Pandemia</span>)

- **Spearman**: Coeficiente = 0,6714; Valor-p = 0,0001  
- **Pearson**: Coeficiente = 0,6323; Valor-p = 0,0004  

Este semestre, o único do período pós-pandemia até o momento, ele apresenta as correlações mais fortes de todos os semestres analisados. Ambos os coeficientes são altos e estatisticamente significativos, indicando uma correlação positiva forte entre frequência e desempenho. Esses resultados sugerem que a ação de extensão pode ter tido um impacto ainda mais importante para os alunos após o retorno das aulas presenciais.

### Conclusões (Preciso do ultimo semestre ainda)

---

### Diagrama do Fluxo de Execução

```mermaid
graph LR
A[Conversão dos Arquivos PDF para XLSX/CSV] -->
B[Tratamento de Dados Ausentes] -->
C[Padronização de Formatos] -->
D[Redução de Colunas] -->
E[Normalização dos Dados]
```

Essa abordagem oferece uma visão mais resumida e fácil de entender, além de permitir que a análise seja focada não só na frequência, mas também no desempenho dos alunos na disciplina. Dessa forma, ficou mais simples comparar o impacto da frequência no rendimento acadêmico e no status final de aprovação.

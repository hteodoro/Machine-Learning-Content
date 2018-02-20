
import numpy
import pandas

# Um dos objetos principais da biblioteca pandas são as Series
# As Series funcionam como um dicionário de python
# É possível construi-las com listas, numpy arrays e etc
# O primeiro argumento é o array ou lista, o segundo são labels para os dados
if False:
    list_series = pandas.Series(['Hen', 'Thi', 'Vit', 'Mat'], [1, 2, 3, 4])
    print(list_series)
    # Construindo uma Series a partir de um numpy array
    array_series = pandas.Series(numpy.array(list_series))
    print(array_series)


# Outro Objeto principal da biblioteca são os DataFrames
# O objetivo do DataFrame é construir uma tabela de dados com os dados passados
# O primeiro parametro é o vetor, matriz ou dicionario que você deseja transformar em um dataframe
# O segundo parametro são os indexes ('linhas'), o terceiro são as columns ('colunas')
if False:
    data_frame = pandas.DataFrame(numpy.random.randn(4, 4), 'A B C D'.split(), 'W X Y Z'.split())
    print(data_frame)
    # É possível fazer a seleção de elementos de um dataframe utilizando os colchetes
    if False:
        data = data_frame['W']
        print(data)
    # Também é possível fazer uma seleção multipla
    if False:
        data = data_frame[['W', 'X']]
        print(data)
    # Também é possível fazer seleção com base nos indices utilizando o loc[]
    if False:
        data = data_frame.loc['A']
        print(data)
    # Também é possível fazer seleção multipla com loc[]
    if False:
        data = data_frame.loc[['A', 'C'], ['W', 'X']]
        print(data)
    # Se deseja utilizar índices numéricos comos de um array ou lista,utilize o iloc[]
    if False:
        data = data_frame.iloc[:2, 1:3]
        print(data)

# Também é possível fazer uma seleção condicional em DataFrames
if False:
    data_frame = pandas.DataFrame(numpy.random.randn(3, 3), 'A B C'.split(), 'W X Y'.split())
    print(data_frame)
    # Fazendo uma seleção condicional
    data = data_frame[data_frame['W'] > 1]
    print(data)
    # Fazendo uma seleção condional e especificando uma coluna
    data = data_frame[data_frame['W'] > 1]['Y']
    print(data)
    # Você também pode realizar uma seleção condicional com operações lógicas
    data = data_frame[(data_frame['W'] > 1) & (data_frame['Y'] > 0)]
    print(data)

if False:
    # Os DataFrames lhe permitem inserir novos dados na tabela já criada
    data_frame = pandas.DataFrame(numpy.random.rand(4, 4))
    data_frame['new'] = pandas.Series(numpy.array('6 8 12 5'.split()))
    print(data_frame)
    # Você também pode apagar dados com o método drop
    # O parametro axis define se a coluna já estava presente na formação original ou não
    # 0 para coluna original, 1 para pós adicionada
    # O parametro inplace define se você deseja manter a alteração no DataFrame original
    data_frame.drop('new', axis=1, inplace=True)
    print(data_frame)


### VALORES NULOS NaN ###
if False:
    # Existem dois métodos de DataFrame para a manipulação de valores nulos (NaN)
    # O dropna() é usado para remover uma coluna ou linha que não possua valores
    data = pandas.Series(['Henrique', 'Thiago', 'Matheus', numpy.nan])
    data_frame = pandas.DataFrame(data)
    print(data_frame)
    # utilize o dropna() para dropar colunas ou linhas
    if False:
        data_frame.dropna(axis='columns', how='any', inplace=True) # Excluir coluna onde exista pelo menos um valor NaN
        print(data_frame)

    if False:
        data_frame.dropna(axis='index', how='all', inplace=True) # Excluir linha onde todos valores são NaN
        print(data_frame)

    # o fillna() é usado para preencher valores NaN com informações definidas
    if False:
        data_frame.fillna('Jonas', inplace=True) # Setando TODOS valores NaN como 'Jonas'
        print(data_frame)


### AGRUPAMENTOS E JUNÇÕES ###
if False:
    # Construindo o data frame
    data = {'team': ['PSG', 'PSG', 'Real Madrid', 'Real Madrid', 'Bayern'],
            'player': ['Neymar', 'mBape', 'Ronaldo', 'Bale', 'Levandowisk'],
            'goals': [2, 1, 3, 2, 5]}
    # Instanciando o data frame com a data
    data_frame = pandas.DataFrame(data)
    print(data_frame)
    # É possível agrupar informações por colunas em dataframes
    team_group = data_frame.groupby('goals')
    # Com informações agrupadas, é possível realizar funções matemáticas para resultados especificos
    print(team_group.sum())
    print(team_group.mean())
    # Utilizando o método describe() você é capaz de ter uma visualização mais direta
    print(team_group.describe())

### LEITURA DE ARQUIVOS ###
# Com a biblioteca pandas é possível ler junções de dados em diferentes tipos de arquivos
# É possível ler dados de arquivos csv (comma separated values), Excel, JSON e até HTML
# csv's são os principais, podemos utilizar o método read_csv()
if False:
    data_frame = pandas.read_csv('csv/example.csv')
    # também é possível exportar um dataframe qualquer para um modelo csv
    data_frame.to_csv('csv/exported.csv', encoding='utf-8')

### MÉTODOS IMPORTANTES ###
if True:
    # É possível retornar uma Series com a frequencia de valores utilizando o método value_counts()
    data = {'team': ['PSG', 'PSG', 'Real Madrid', 'Real Madrid', 'Bayern'],
            'player': ['Neymar', 'mBape', 'Ronaldo', 'Bale', 'Levandowisk'],
            'goals': [2, 1, 3, 2, 5]}
    # Instanciando data frame
    data_frame = pandas.DataFrame(data)
    print(data_frame)
    # Printando Series de frequencia, tabela de frequencia
    print(data_frame['team'].value_counts())

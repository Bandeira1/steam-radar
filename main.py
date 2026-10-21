import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# O cabeçalho do games.csv junta "Discount" e "DLC count" em uma coluna só,
# então lemos o cabeçalho, separamos essas duas e pulamos a linha original
colunas = pd.read_csv('games.csv', nrows=0).columns.tolist()
i = colunas.index('DiscountDLC count')
colunas[i:i + 1] = ['Discount', 'DLC count']

# Colunas usadas na análise: identificação, gênero/categoria, preço,
# avaliação dos jogadores, popularidade e data de lançamento
usar = ['AppID', 'Name', 'Genres', 'Categories', 'Price',
        'Positive', 'Negative', 'Estimated owners', 'Release date']
df = pd.read_csv('games.csv', names=colunas, header=0, index_col=False, usecols=usar)
df = df[usar]

print(df.head(5))

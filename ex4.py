import pandas as pd

dados = pd.read_csv('data/paises.csv', sep=';', encoding='utf-8')

# a) Selecionar e exibir os países que estão na região da Oceania
paises_oceania = dados[dados['Region'].str.contains('OCEANIA', case=False)]
print("Países da região da OCEANIA:") 
print(paises_oceania['Country'].values)

# b) Contar o número de países na Oceania
quantidade_paises_oceania = paises_oceania['Country'].count()
print(f'\nNúmero total de países na OCEANIA: {quantidade_paises_oceania}')

# c) Calcular a média da taxa de alfabetização, ignorando valores ausentes
media_alfabetizacao = dados['Literacy (%)'].mean(skipna=True)
print(f'\nMédia da taxa de alfabetização: {media_alfabetizacao:.2f}%')

# d) Encontrar o país com a maior população
pais_maior_populacao = dados.loc[dados['Population'].idxmax(), ['Country', 'Region']]
print("\nPaís com a maior população:")
print(pais_maior_populacao.to_string(index=False))

# e) Filtrar os países sem costa marítima e salvar em um novo arquivo CSV
paises_sem_costa = dados[dados['Coastline (coast/area ratio)'] == 0]
paises_sem_costa.to_csv('no-coast-countries.csv', index=False, encoding='utf-8')

import matplotlib.pyplot as plt
import pandas as pd


# 1
# dfEmpresas = pd.read_csv('data/space.csv', delimiter=';')

# dfEmpresas = dfEmpresas.drop_duplicates(subset='Company Name')
# empresas_EUA = dfEmpresas['Location'].str.contains('USA').sum()
# empresas_CHINA = dfEmpresas['Location'].str.contains('China').sum()

# print('Empresas dos EUA:', empresas_EUA)
# print('Empresas dos CHINA:', empresas_CHINA)
# plt.bar(['EUA', 'CHINA'], [empresas_EUA, empresas_CHINA], color=['blue', 'red'])
# plt.xlabel('País')
# plt.ylabel('Número de empresas')
# plt.title('Empresas por país')
# plt.savefig('empresas_por_pais.png')
# plt.show()

# 2
dfPaises = pd.read_csv('data/paises.csv', delimiter=';')

northern_america_countries = dfPaises[dfPaises['Region'] == 'Northern America']

plt.plot(northern_america_countries['Country'], northern_america_countries['Deathrate'], label='Deathrate', color='red')
plt.plot(northern_america_countries['Country'], northern_america_countries['Birthrate'], label='Birthrate', color='blue')

plt.xlabel('País')
plt.ylabel('Taxa')
plt.title('Taxa de natalidade e mortalidade por país')
plt.legend()
plt.savefig('taxa_natalidade_mortalidade.png')
plt.show()

import numpy as np
arr = np.loadtxt('data/paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# 1
print(arr[:, [0, 1, 2, 3]])

# 2
regioes = arr[:, 1]

print(np.unique(regioes, return_counts=True))

# 3
literacy = arr[1:, 9].astype(float)

print(np.mean(literacy))

# 4
regions = np.char.strip(arr[1:, 1])
paises_north_america = np.sum(regions == 'NORTHERN AMERICA')

print(paises_north_america)

# 5 
countries = arr[1:, 0]  
regions = arr[1:, 1]    
gdp_values = arr[1:, 9].astype(float)  

latin_america_indices = np.char.strip(regions) == "LATIN AMER. & CARIB"

latin_america_countries = countries[latin_america_indices]
latin_america_gdp = gdp_values[latin_america_indices]


max_gdp_index = np.argmax(latin_america_gdp)

country_with_max_gdp = latin_america_countries[max_gdp_index]
max_gdp = latin_america_gdp[max_gdp_index]

print(f"País da América Latina e Caribe com a maior renda per capita: {country_with_max_gdp} com GDP: {max_gdp}")

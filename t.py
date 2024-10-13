import numpy as np

arr = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

#Questão 1 
data_sliced = arr[:, [0, 1, 2, 3]]

print(data_sliced)

#Questão 2
regions = arr[:, 1]

unique_regions = np.unique(regions)
print(f"Número de regiões únicas: {len(unique_regions)}")
print("Regiões encontradas:")
for region in unique_regions:
    print(region)

#Questão 3
literacy_rates = arr[1:, 9]

valid_literacy_rates = literacy_rates[literacy_rates != '']

literacy_rates_float = valid_literacy_rates.astype(float)

average_literacy_rate = np.mean(literacy_rates_float)

print(f"Taxa média de alfabetização global: {average_literacy_rate:.2f}%")

#Questão 4
regions = arr[1:, 1]

northern_america_count = 0

for region in regions:
    if region.strip() == "NORTHERN AMERICA":
        northern_america_count += 1

print(f"Número de países na América do Norte: {northern_america_count}")

#Questão 5
countries = arr[1:, 0]
regions = arr[1:, 1] 
gdp_values = arr[1:, 9].astype(float)  


max_gdp = -1
country_with_max_gdp = ""

for i in range(len(regions)):
    if regions[i].strip() == "LATIN AMER. & CARIB":
        if gdp_values[i] > max_gdp:
            max_gdp = gdp_values[i]
            country_with_max_gdp = countries[i]

print(f"País da América do Sul e Caribe com a maior renda per capita: {country_with_max_gdp} com GDP: {max_gdp}")

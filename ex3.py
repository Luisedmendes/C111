import numpy as np
arr = np.loadtxt('data/space.csv', delimiter=';', dtype=str, encoding='utf-8')
# # 1
# status_missoes = arr[:, -1]

# status_missoes = np.where(status_missoes == 'Success', 1, 0)

# porcentagem = np.mean(status_missoes) * 100

# print(porcentagem)

# # 2

# custos = arr[:, -2]

# custos_numbers = custos[1:].astype(float)

# print(np.mean(custos_numbers) * 100)

# # 3

# locations = arr[:, 2]

# in_usa = np.array([1 if "USA" in location else 0 for location in locations])

# usa_missions = 0
# for x in in_usa:
#   if x == 1: usa_missions += 1

# print(usa_missions)  

# 4

companys = arr[:, 1]

costs = arr[:, -2]

custos_numbers = costs[1:].astype(float)

spacex_filter = np.where(companys == 'SpaceX')
print(spacex_filter)

spacex_costs = costs[spacex_filter]

max_cost_idx = np.argmax(spacex_costs)

most_expensive_mission_idx = spacex_filter[0][max_cost_idx]
most_expensive_mission = arr[most_expensive_mission_idx]

print(most_expensive_mission)

# 5
# company_names = arr[:, 1]

# company_missions_count = {}

# for company in company_names:
#     if company in company_missions_count:
#         company_missions_count[company] += 1
#     else:
#         company_missions_count[company] = 1

# print("Empresas e quantidades de missões realizadas:")
# for company, count in company_missions_count.items():
#     print(f"Empresa: {company}, Quantidade de missões: {count}")





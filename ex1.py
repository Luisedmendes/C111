# 1 (Utilizando tabela da LaLiga 2023

table = [
  'Barcelona',
  'Real Madrid',
  'Atlético Madrid',
  'Real Sociedad', 
  'Vilarreal'
] 


# a) 3 primeiros colocados
# print(table[0:3])

# # b) Os ultimos dois colocados
# print(table[3:])

# # c) lista em ordem alfabeticas
# def getFIrstLetter(team):
#   return str(team[0]).lower()

# def filterTeams(table):
  alfabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'x', 'y', 'z']
  result = []
  for team in table:
    index = alfabeth.index(getFIrstLetter(team))
    result.insert(index, team)
  return result

# print(filterTeams(table=table))

# 2
# loja1 = {'samsung', 'nokia', 'apple'}  
# loja2 = {'motorola', 'xiaomi', 'huawei'}

# total = loja1.union(loja2)
# print(total)
# print(loja1)
# print(loja2)

# # 3
# def handleResult(name, media):
#   data = {'name': name, 'media': media}
#   if (data.get('media') >= 60):
#     data.update({'sitation': 'AP'})
#   else:
#     data.update({'sitation': 'RP'})
#   return data

# name = input('Entre com um nome ')
# media = int(input('Entre com a media '))

# print(handleResult(name=name, media=media))






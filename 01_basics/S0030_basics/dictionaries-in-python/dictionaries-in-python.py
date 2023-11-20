

house = { 'street': 'broadway', 'number': 87 }

print(house) # {'street': 'broadway', 'number': 87} output = {'street': 'broadway', 'number': 87}

print(len(house)) # 2 output = 2

house['floors'] = 4
print(house) # {'street': 'broadway', 'number': 87, 'floors': 4} output = {'street': 'broadway', 'number': 87, 'floors': 4}

print(house['street']) # broadway output = broadway

print(len(house)) # 3 output = 3

print(house.keys()) # ['street', 'number', 'floors'] output = dict_keys(['street', 'number', 'floors'])

print(house.values()) # ['broadway', 87, 4] output = dict_values(['broadway', 87, 4])
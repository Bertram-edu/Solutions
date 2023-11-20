

numbers = [5, -2, 4, 17]

print(type(numbers)) # list
print(len(numbers)) # 4
print(17 in numbers) # True
print(2 in numbers) # false
print(numbers[0]) # 5
print(numbers[3]) # 17
print(numbers[-1]) # 17
print(numbers[:2]) # [5, -2]
print(numbers[2:]) # [4, 17]
numbers.append(9) # [5, -2, 4, 17, 9]
numbers.append(5) # [5, -2, 4, 17, 9, 5]

print(numbers) # [5, -2, 4, 17, 9, 5]
print(numbers[2:]) # [4, 17, 9, 5]
print(len(numbers)) # [5, -2, 4, 17, 9, 5]
print(sorted(numbers)) # [-2, 4, 5, 5, 9, 17]
print(numbers) # [5, -2, 4, 17, 9, 5]
numbers.sort() # [-2, 4, 5, 5, 9, 17]

print(numbers) # [-2, 4, 5, 5, 9, 17]
print(numbers) # [-2, 4, 5, 5, 9, 17]


print(numbers[1]) # 4
print(numbers[5]) # 17
print(numbers[2:4]) # [5, 5]
print(numbers[3:6]) # [5, 9, 17]

numbers.append(3)
print(numbers) # [-2, 4, 5, 5, 9, 17, 3]

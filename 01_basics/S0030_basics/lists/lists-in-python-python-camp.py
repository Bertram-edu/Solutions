

dogs = ["Roger", "Syd"]

items = ["Roger", 1, "Syd", True]

print("Roger" in items) # True

items[0] = "Roger"

print(items[0]) # "Roger"
print(items[1]) # 1
print(items[3]) # True

print(items[-1]) # True

print(items[0:2]) # ["Roger", 1]
print(items[2:]) # ["Syd", True]

print(len(items)) #4

print(items[0:])

items.append("Test_1")
items.extend(["Test_2"])
items += ["Test_3"]
print(items[0:])

items.remove("Test_1")

print(items[0:])


items += ["Test1", "Test2"]

#or

items.extend(["Test1", "Test2"])

print(items[0:])

items.insert(1, "Test") # add "Test" at index 1

print(items)

items[1:1] = ["Test1", "Test2"]

print(items)

items.remove(1)

items.remove(True)

print(items)

itemscopy = items[:]

print(items)

print(itemscopy)

print(sorted(items, key=str.lower))

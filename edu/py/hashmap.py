#HashMap

myMap = {}
myMap["Jason"] = 1
myMap["Matteo"] = 2
print(myMap)
print(len(myMap))

myMap["Luca"] = 3
print(myMap["Luca"])

myMap.pop("Jason")
print("Jason" in myMap)

# Dict comprehention
myMap = { i: 2*i for i in range(3)}
print(myMap)

# Loops
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

# unpacking
for key, val in myMap.items():
    print(key, val)


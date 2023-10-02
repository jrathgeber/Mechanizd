#Hashset

myset = set()

myset.add(1)
myset.add(2)
myset.add(2)

print(myset)
print(len(myset))

print(1 in myset)
print(7 in myset)

myset.remove(2)
print(2 in myset)

# list to set
print(set([1,2,3]))

#comprehensio
mySet = {i for i in range(5)}
print(mySet)


# Division -> decimal
print(5/2)
print(5//2)
print(-3//2)

#workaround
print(int(-3/2))

# Modulo
print(10%3)

# no worky for negs
print(-10%3)

# otherwise

import math
print(math.fmod(-10,3))     # = -1
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))

# infinity
float("inf")
float("-inf")

# Python numbers are infinit
print(math.pow(2,200))

# check is less than
print(math.pow(2,200) < float("inf"))



# sort string
arrs = ["Jason", "Matteo", "Luca", "Fabio"]
arrs.sort()
print(arrs)

# custom sort (by length od string)
arrs.sort(key=lambda x: len(x))
print(arrs)


# list comprehension
arr = [i for i in range(5)]
print(arr)

# list comprehension
arr = [i+1 for i in range(5)]
print(arr)

# 2 d list
arr = [[0] * 4 for i in range(4)]
print(arr)

# with math
result = [i * 2 for i in range(10)]
print(result)
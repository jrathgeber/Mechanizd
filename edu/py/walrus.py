# Simplify while loop
file = open("a1.py", "r")
while line := file.readline():
    print(line)

# stream line if
if author := "Jason":
    print(f'The author is {author}.')


list1 = [1,2,3]

# List comprehension
results = []
for x in list1:
    y = x+1
    if y > 0:
        results.append((x, y))
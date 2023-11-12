# Testing python hints

# a should be an int
# b should be an int
# the function's return type should be an int
def add(a:int, b:int) -> int:
    return a + b

x = add(4, 5)      # x = 9

print(x)

# not following type hints
y = add('hello', 'world')      # x = 'helloworld'

print(y)
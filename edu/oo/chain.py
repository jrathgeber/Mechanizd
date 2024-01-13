class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, amount):
        self.value += amount
        return self  # Return self to allow chaining

    def multiply(self, factor):
        self.value *= factor
        return self

    def subtract(self, amount):
        self.value -= amount
        return self


# Using the class with method chaining
result = Calculator(10).add(5).multiply(2).subtract(3).value
print(result)
# 27
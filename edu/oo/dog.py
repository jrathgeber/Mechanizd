class Dog:
    # behaviour when Dog object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # behaviour when str(dog_object) is called
def __str__(self):
    return f'Dog({self.name}, {self.age})'

    # behaviour when dog1 == dog2 happens
def __eq__(self, otherDog):
    return self.name == otherDog.name and self.age == otherDog.age
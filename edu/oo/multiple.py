# multiple inheritance in python

class A:
    def speak(self):
        print('A')

class B:
    def speak(self):
        print('B')

# C inherits from both A and B
class C(A, B):
    pass

C().speak()     # A
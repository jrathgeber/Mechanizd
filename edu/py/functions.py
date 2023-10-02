# functions

def myFunc(n,m):
    return n * m

# Nested

def outer(a,b):
    c = "c"

    def inner():
        return a + b +c

    return inner();

print (outer("a", "b"))



# can modify objects but not reassign

def double(arr, val):
    def helper():
        for i, n in enumerate(arr):
            arr[i] *= 2

        # looks out for scope here
        nonlocal val
        val *=2
    helper()
    print(arr, val)

nums = [1,2]
val = 3
double(nums, val)



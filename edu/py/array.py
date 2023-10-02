# python code to create an array

# this was here before from somewhere
import array as arry
a = arry.array('i', [1, 2, 3])
print ("The new created array is : ", end=" ")

for i in range(0, 3) :
    print(a[i], end="")
print()


# simple from neet code October 2nr
print("neet")
arr = [1, 2, 3]
arr.append(4)
print (arr)

# Pop
arr.pop()
print(arr)

arr.insert(1,7)

arr[0] = 0
arr[3] = 0
print(arr)

# initialize
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# get last value
print(arr[-1])

# slice it
print(arr[1:3])

# unpacking
a,b,c = [1,2,3]

# loop through it
for i in range (len(arr)):
    print(arr[i])

# no index
for n in arr:
    print(arr[n])

# with index and value
for i, n, in enumerate (arr):
    print(i, n)

# zip

nums1 = [1,3,5]
nums2 = [2,4,6]

for n1, n2 in zip(nums1, nums2):
    print(n1,n2)

# reverse
nums1.reverse()
print("jason")
print(nums1)

# sorting
arrx = [5,4,7,3,8]
arrx.sort()
print(arr)

arrx.sort(reverse=True)

# sort string
arrs = ["Jason", "Matteo", "Luca", "Fabio"]
arrs.sort()
print(arrs)

# custom sort (by length od string)
arrs.sort(key=lambda x: len(x))
print(arrs)




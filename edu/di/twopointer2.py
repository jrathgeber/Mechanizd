
def twoSum (a, target):
    # start
    i = 0
    #end
    j = len(a)-1
    while i < j:
        sm = a[i]+a[j]
        if target == sm:
            print("{} {}".format(a[i], a[j]))
            print("{} {}".format(i,j))
            return True
        elif sm < target:
            i=i+1
        else:
            j=j-1
    return False

t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    target = int(input())
    print(twoSum(a, target))

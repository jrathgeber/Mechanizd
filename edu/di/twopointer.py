def isPalindome(s):
    # start
    i = 0
    #end
    j = len(s)-1
    while i<j:
        if s[i] != s[j] :
            return False

        i=i+1
        j=j-1
    return True


t = int(input())
for i in range(t):
    s = str(input())
    print(isPalindome(s))

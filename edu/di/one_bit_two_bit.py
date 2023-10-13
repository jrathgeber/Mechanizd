from typing import List


#We have two special characters:
#The first character can be represented by one bit 0.
#The second character can be represented by two bits (10 or 11).
#Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

#Example 1:
#Input: bits = [1,0,0]
#Output: true

#Example 2:
#Input: bits = [1,1,1,0]
#Output: false


def isOneBitCharacter(bits: List[int]) -> bool:
    i = 0
    n = len(bits)
    numbits = 0
    while i < n:
        if bits[i] == 1:
            i += 2
            numbits += 2
        else:
            i += 1
            numbits = 1
    return numbits == 1

x = isOneBitCharacter([1, 0, 0])

print(x)

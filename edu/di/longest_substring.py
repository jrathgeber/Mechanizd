# -*- coding: utf-8 -*-

"""

Created on Thu Dec  5 11:14:40 2019

@author: not me came from interweb I think stack overflow

https://codereview.stackexchange.com/questions/197589/given-a-string-find-the-length-of-the-longest-substring-without-repeating-chara

"""

class Solution:
   
    # Nicely O squared
    
    def lengthOfLongestSubstring(self, word):
        n = len(word)
        longest = 0
        for i in range(n):                      # Range Creates a sequence from 0 to Length
            print(i)
            seen = set()                        # Create a Set
            for j in range(i, n):
                if word[j] in seen: break
                seen.add(word[j])
            longest = max(len(seen), longest)   # The old length of string vs length of set thing 
        return longest      
          
      
print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10

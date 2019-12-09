# -*- coding: utf-8 -*-
"""

Created on Sat Dec  7 14:53:57 2019

@author: Jason

A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/


"""


class Solution: 
    #def longestPalindrome(self, s):
      # Fill this in.
        
    # A O(n^2) time and O(1) space program to find the  
    #longest palindromic substring 
  
    # This function prints the longest palindrome substring (LPS) 
    # of str[]. It also returns the length of the longest palindrome 
    def longestPalindrome(self, s):
        maxLength = 1
      
        start = 0
        length = len(string) 
      
        low = 0
        high = 0
      
        # One by one consider every character as center point of  
        # even and length palindromes 
        for i in xrange(1, length): 
            # Find the longest even length palindrome with center 
        # points as i-1 and i. 
            low = i - 1
            high = i 
            while low >= 0 and high < length and string[low] == string[high]: 
                if high - low + 1 > maxLength: 
                    start = low 
                    maxLength = high - low + 1
                low -= 1
                high += 1
      
            # Find the longest odd length palindrome with center  
            # point as i 
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and string[low] == string[high]: 
                if high - low + 1 > maxLength: 
                    start = low 
                    maxLength = high - low + 1
                low -= 1
                high += 1
      
        print ("Longest palindrome substring is:") 
        print (string[start:start + maxLength] )
      
        return maxLength   
      
      
      
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar


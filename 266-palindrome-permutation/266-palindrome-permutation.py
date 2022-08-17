from collections import Counter 

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        odd_char_count = 0  # count number of keys with odd values
        freq = Counter(s)  # frequency table
        
        # iterate over values 
        for value in freq.values():
            if value % 2 == 1:
                odd_char_count += 1
        
        return odd_char_count < 2
        
        
        
        
        
    
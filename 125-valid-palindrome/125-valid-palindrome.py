class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # edge case only consider chars that are alphanumeric (c.isalnum())
        p1, p2 = 0, len(s) - 1 
        
        # iterate from ends inward 
        while p1 < p2: 
            
            # skip non alphanumeric chars
            if not s[p1].isalnum(): 
                p1 += 1 
                continue
                    
            if not s[p2].isalnum():
                p2 -= 1
                continue
            
            # compare curr chars, convert to lower
            if s[p1].lower() != s[p2].lower(): 
                return False
        
            p1 += 1
            p2 -= 1
        
        return True 
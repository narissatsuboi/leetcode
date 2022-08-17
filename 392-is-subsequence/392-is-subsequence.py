class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        2ptr approach
        tc: O(n) sc: O(1)
        """
        # init pointers 
        ptr_s, ptr_t = 0, 0 
        
        # store bounds
        n_s, n_t = len(s), len(t)
        
        # iterate over t until c in s is found in t 
        while ptr_s < n_s and ptr_t < n_t:
            
            if s[ptr_s] == t[ptr_t]: 
                ptr_s += 1
            ptr_t += 1
            
        return ptr_s == n_s
        
        
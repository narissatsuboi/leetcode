class Solution:
    
    # 2 HashMaps, simpler than #1 HashMap
    def isAnagram(self, s: str, t: str) -> bool:
        """
        TC: O(n)
        SC: O(n)
        """
        
        # check s and t same length 
        if len(s) != len(t):
            return False
        
        # fill hashmaps for s and t 
        countS, countT = {}, {}
        
        for charS, charT in zip(s, t):
            countS[charS] = countS.get(charS, 0) + 1
            countT[charT] = countT.get(charT, 0) + 1

        # iterate over each hashmap for s and check count 
        # matches in hashmap for t 
        for charS in countS:
            if countS[charS] != countT.get(charS, 0):
                return False
        
        return True 
        
    
    
#     # 1 HashMap 
#     def isAnagram(self, s: str, t: str) -> bool:
#         """
#         Returns true is strings are anagrams. 
        
#         TC: O(n)
#         SC: O(n)
        
#         :param s: first string to compare
#         :param t: second string to compare
#         :rtype: bool 
#         """
        
#         # check lengths of strings are same 
#         if len(s) != len(t):
#             return False
        
#         # populate frequency table with s 
#         s_freq = {}
#         for char in s:
#             if char not in s_freq:
#                 s_freq[char] = 1
#             else:
#                 s_freq[char] += 1
        
#         # iterate over t, update frequency table
#         for char in t:
#             if char not in s_freq:
#                 return False
#             s_freq[char] -= 1
        
#         # iterate over frequency table, check all values are 0 
#         for value in s_freq.values():
#             if value != 0:
#                 return False
        
#         return True
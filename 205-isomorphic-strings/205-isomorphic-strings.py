class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        brief: determine if s and t are isomorphic 
        s, t: equally sized, non empty strings
        returns: True if isomorphic 
        """
        
        # must ensure 1 to 1 mapping 
        # init 2 hashmaps for each string 
        mapST, mapTS = {}, {}
        
        # traverse the strings at same position 
        for c1, c2 in zip(s, t):
            
            # detect if another mapping already exists in both maps
            if((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            
            # map characters
            mapST[c1] = c2
            mapTS[c2] = c1
            
        return True 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        TC (n2)
        SC (n)
        """
        
        # init anagram dict { tuple(1, 0, 0 ... 2) : ["bat, tab"]}
        res = defaultdict(list)
        
        # iterate over list 
        for s in strs:
            counts = [0] * 26  #[a......z]
            
            # iterate over chars in element 
            for c in s: 
                # update count of c in counts
                counts[ord(c) - ord("a")] += 1
                
            # store s in values array inside of dict
            res[tuple(counts)].append(s)  # change count to tuple 
            
            
        
        return res.values()
        
        
        
        
        
        
        
                
            
            
            
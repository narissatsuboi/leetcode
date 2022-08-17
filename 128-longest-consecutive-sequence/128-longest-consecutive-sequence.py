class Solution: 
    
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        TC O(n)
        SC O(n)
        """
            
        
        numSet = set(nums) # list to set 
        longest = 0        # longest sequence found
        
        # check if current num is the start of a set 
        for num in nums:
            # found start of a sequence
            if num -1 not in numSet: 
                
                length = 0
            
                # look for next num in the sequnce 
                while (num + length) in numSet:
                    length += 1 
                longest = max(length, longest)
        return longest
        
        
        
            
    # def longestConsecutive(self, nums: List[int]) -> int:
        
#         # list of consecutive nums found
#         result = []  
        
#         # {100 : False, 4 : False, 200 : False, 1 : False, 3 : False, 2 : False }
#         haveSeen = dict.fromkeys(nums, False)  
        
#         for num in nums: 
            
#             # store nums before and after current num 
#             before, after = num - 1, num + 1
            
            
#             # check to add num to haveSeen
#             haveSeen[num] = True
            
#             # check if before and or after has been seen 
#             if haveSeen.get(before,False) == True and before not in result: 
#                 result.append(before)
                
#                 # add num to result if not in 
#                 if num not in result:
#                     result.append(num)
                
#             if haveSeen.get(after, False) == True and after not in result:
#                 result.append(after)
                
#                 # add num to result if not in 
#                 if num not in result:
#                     result.append(num)
        
#         return len(result)
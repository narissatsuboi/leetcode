class Solution:
    
#     # Brute Force Nested Loops 
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         """
#         TC: O(n2)
#         SC: O(1)
#         """
        
#         # iterate along length of array nums
#         for i in range(len(nums)):
#             first_num = nums[i]
            
#             # check along remainder of array for matching
#             for j in range(i+1, len(nums)):
#                 second_num = nums[j]
#                 if first_num + second_num == target:
#                     return [i, j]
                
    # One Pass HashMap 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        TC: O(n)
        SC: O(n)
        """

        prevMap = {}  # map if elements we've come across in nums {value: index}

        # iterate over array 
        for idx, val in enumerate(nums):
            diff = target - val

            # value - curr num == target, return indices 
            if diff in prevMap:
                return [prevMap[diff], idx]

            # check value - curr num != target? store in hashmap 
            prevMap[val] = idx 
            
    
            
            
        
        
        
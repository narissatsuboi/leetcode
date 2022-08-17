class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        2 pointer solution 
        TC: O(n) SC: O(1)
        """
        
        # init pointers 
        left, right = 0, len(numbers)-1
        
        
        # iterate ptrs while they have not crossed 
        while left < right: 
            # sum nums at left and right ptrs
            curr_sum = numbers[left] + numbers[right]
            
            # compare sum to target 
            if curr_sum < target: 
                # move left pointer in
                left += 1
            elif curr_sum > target: 
                # move right pointer in 
                right -= 1
            else:
                # condition met 
                return [left+1, right+1]  # +1 for 1-index requirement        
            
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         """
#         Brute force solution with nested loops 
#         TC: O(n2) SC: O(1)
#         """
        
#         for i in range(len(numbers)):
#             for j in range(i+1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i+1, j+1]
#         return []
    
    
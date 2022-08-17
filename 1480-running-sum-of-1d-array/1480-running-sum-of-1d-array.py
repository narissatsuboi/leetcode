class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
#         # init pointer
#         reader, writer = 0, 1
                
#         while writer < len(nums):
#             # store result sum in each running index
#             nums[writer] = nums[reader] + nums[writer]
            
#             # update pointer
#             reader += 1
#             writer += 1 
            
#         return nums
    
    
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        return nums
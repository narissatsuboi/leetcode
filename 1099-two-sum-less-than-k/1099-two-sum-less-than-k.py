class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """
        Sort the input array and use 2 ptr approach
        TC:O(nlogn) Python sort nlogn 
        SC: O(1)
        """
        
        # sort the array in non descending order 
        nums.sort() 
        
        # init ptrs 
        left, right = 0, len(nums) - 1 
        
        max_sum = -1
        
        while left < right: 
            curr_sum = nums[left] + nums[right]
            if nums[left] + nums[right] < k:
                max_sum = max(max_sum, curr_sum)
                left += 1
            else: 
                right -=1 
        
        return max_sum
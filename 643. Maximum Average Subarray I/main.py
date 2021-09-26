"""
643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error
less than 10-5 will be accepted.
"""

import math

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        Sliding Window
        Constraints: (1) Max avg (2) Subarray size K
        :type nums: List[int]
        :type k: int
        :rtype: float

        nums = [1,12,-5,-6,50,3], k = 4
                              i

        """

        # max_avg return value -10**5
        max_avg = -10**4 - 1
        # current_running_avg holds avg of current window
        current_running_avg = 0.0
        current_running_sum = 0.0

        for i in range(len(nums)):
            current_running_sum += nums[i]
            current_running_avg = current_running_sum/k

            # compare max_avg and current_running_avg
            if i >= k-1:
                # update max_avg
                max_avg = max(max_avg, current_running_avg)
                # shrink the window
                current_running_sum -= nums[i - (k-1)]

        return max_avg


if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    print(Solution.findMaxAverage(Solution, nums,k))
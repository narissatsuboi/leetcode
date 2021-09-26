"""
209. Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return
the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is greater than or equal to target. If there is no such
subarray, return 0 instead.

target = 7, nums = [2,3,1,2,4,3]

Psuedocode
Iterate over array with windowEnd index
windowStart index dynamically adjusts when target constraint is met
Update the running sum when window is shortened
Store minimum window size at each extension
Compare current size with minimum window size from previous iteration
Return minimum window size
"""

import math
import sys


def find_min_size_subarray(arr, target):
    window_start = 0  # pointer to track left window position
    min_window_size = 10 ** 5 + 1  # store minimum window size encountered
    running_sum = 0  # accumulator

    # for loop, loop control var is windowEnd
    for window_end in range(len(arr)):
        # update window sum
        running_sum += arr[window_end]

        # when constraint is met
        while running_sum >= target:
            # check if current window size is smaller than the stored size,
            # update min_window_size
            min_window_size = min(min_window_size, (window_end - window_start)
                                  + 1)

            # base case size is 1 -> return
            if min_window_size == 1:
                return min_window_size

            # shrink window and adjust sum
            running_sum -= arr[window_start]
            window_start += 1

    return min_window_size


if __name__ == '__main__':
    target = 7
    arr = [2, 3, 1, 2, 4, 3]
    print(arr)
    print(find_min_size_subarray(arr, target))

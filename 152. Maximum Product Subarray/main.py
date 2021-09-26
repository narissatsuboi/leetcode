"""
SITUATION
# Understand the problem
Given an integer array nums, find a contiguous non-empty subarray
within the array that has the largest product, and return the product.
It is guaranteed that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

# Ask clarifying questions
when input array is empty, return 0 or none?

# Confirm Inputs and Outputs
input: int arr
output: max product subarray

# Example
nums = [2,3,-2,4]
       [2,3] -> 6
nums = [-2,0,-1]
       [0] -> 0
nums = [1 2 -2 -4] -> 8
nums = [-2 2 -2 2]
TASK
# Sliding Window
1. start and end pointers of window and move inward
2. store max product
    when product is negative check if
3. compare product of each window to max product

"""





if __name__ == "__main__":
    print("152. Maximum Product Subarray")
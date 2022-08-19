"""
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.

You must write an algorithm that runs in O(n) time and without using t
he division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""
import math

# NOT FAST ENOUGH
# def productExceptSelf(nums):
#     """
#     Brute force solution
#     TC O(n2) for loop + math.prod iterates over lists inside of for loop
#     SC O(1)
#     """
#     answer = []
#
#     # O(N) for loop
#     for i in range(len(nums)):
#         # O(M) for slice
#         answer.append(math.prod(nums[:i]) * (math.prod(nums[i + 1:])))
#
#     return answer # O(N) * O(M) = O(N2)


def productExceptSelf(nums):
    """
    2 array approach
    TC O(n)
    SC O(n)

    :param nums:
    :return:
    """

    # init result to 1
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        # store prefix first
        result[i] = prefix
        # update prefix
        prefix *= nums[i]

    # now result arr holds prefix products
    # next calc postfix products, multiply and store in result
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        # multiply and store postfix into result
        result[i] *= postfix
        #update postfix
        postfix *= nums[i]

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))


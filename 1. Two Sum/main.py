"""
Leetcode 1. Two Sum
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.
You can return the answer in any order.
"""

__version__ = '1'
__author__ = 'Narissa Tsuboi'


def twoSumBrute (nums, target):
    """
    Brute Force approach O(n2).  Compare the sums of each pair with all
    other pairs using a nested for loop. Runtime is very poor.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    n = len(nums)

    for i in range(n):
        for j in range(n):
            sum_ = nums[i] + nums[j]
            #  index cannot pair with itself
            if sum_ == target and i != j:
                return [i, j]


def twoSum(nums, target):
    """
    Hash map approach O(n). Set the values as the keys and the indices as
    the stored dict elements. Then, pass through the map looking for number
    that adds to the target.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    n = len(nums)

    # Initialize empty hash map
    twosum_hash = {}

    # Assign the list elements as the hash map's keys and visa versa
    for i in range(n):
        twosum_hash[nums[i]] = i

    # Find element that when added to the current element in the hash map
    # equals the target and is not nums[i]
    for i in range(n):
        diff = target - nums[i]
        if diff in twosum_hash and twosum_hash[diff] != i:
            return [twosum_hash[diff], i]


if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    # target = 9
    # print(twoSum(nums, target))


    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target))


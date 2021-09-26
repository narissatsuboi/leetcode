"""
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

__author__ = 'Narissa Tsuboi'
__version__ = '1'


def moveZeroes0(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    num_appends = nums.count(0)

    for i in range(num_appends):
        nums.remove(0)
        nums.append(0)

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    pos_last_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[pos_last_zero] = nums[pos_last_zero], nums[i]
            pos_last_zero += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    nums = [0, 1, 0, 3, 12]
    print(nums)
    moveZeroes(nums)
    print(nums)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


def threeSumBF(nums):
    """
    Partial BF solution to 3Sum using 3 for loops
    TC: O(n3) SC: O(1) excluding output
    """

    res = []
    # find all triplets
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])

    # remove duplicate triplets from result
    # use hashmaps, or sort the triplets and for loop

    return res

def threeSum(nums):

    res = []
    nums.sort()

    for i in range(len(nums)):
        # check if ele at i has been seen already
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip iteration

        # 2 pointer combinations
        left, right = i + 1, len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            # sum is less than 0
            if curr_sum < 0:
                left += 1
            # sum is greater than 0
            elif curr_sum > 0:
                right -= 1
            # sum equals 0
            else:  # curr_sum == 0
                # append triplet to result and increment left
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                # but what if left become a dup? need to check dup again
                while nums[left] == nums[left - 1] and left < right:
                    left +=1
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(threeSum(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

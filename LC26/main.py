# 26. Remove Duplicates from Sorted Array
# Narissa Tsuboi 8/15/21

def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # handle lists size 1 or less
    if len(nums) < 2:
        return len(nums)

    # handle lists size 2 or more
    p1 = 0  # slow pointer to track elements to remain, size k - 1

    # compare previous and current element for length of current to end of list
    # p2 fast pointer, find non duplicate numbers
    for p2 in range(1, len(nums)):
        if nums[p1] != nums[p2]:
            p1 += 1  # shift p1 right to element to be updated
            nums[p1] = nums[p2]  # update element at p1 with unique element
                                 # at p2
    k = p1 + 1  # size of sorted, unique array

    return k


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums3 = [1, 1]

    nums1_expected = [1, 2, 2]
    k1_expected = 2

    # test nums 1
    k1 = removeDuplicates(nums1, nums1)
    assert k1 == k1_expected
    for i in range(k1):
        assert nums1[i] == nums1_expected[i]




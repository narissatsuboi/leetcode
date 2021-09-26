"""
Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must appear as many times
as it shows in both arrays and you may return the result in any order.
"""

__name__ = 'Narissa Tsuboi'

import collections


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    counter1 = collections.Counter(nums1)
    counter2 = collections.Counter(nums2)

    return (counter1 & counter2).elements()


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersect(nums1, nums2))

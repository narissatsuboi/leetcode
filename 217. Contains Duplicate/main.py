from collections import Counter

# Narissa Tsuboi
# 217. Contains Duplicate
# 8/15/2021

"""
Brute Force approach would iterate through the array and keep counts of each
item in the array, with counts stored in another array OR going through the
array for every unique element. TC is O(N2). Not even going to implement that.
"""

"""
Counter class (subclass of dict) Use a dict with counter
"""


def containsDuplicate(nums):
    # create Counter (Dict subclass)
    counts = Counter(nums)
    # print(counts)
    # for c in counts:
    #     if counts[c] > 1:
    #         return True
    # return False

    # same approach with hashtable (faster)
    hash_count = {}
    for i in nums:
        if i not in hash_count:
            hash_count[i] = 1
        else:
            return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(nums))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Narissa Tsuboi
# 189. Rotate Array
# 8/15/21

# Approach 1, Brute Force: For every k cycle, move each element one space.
# TC: O(k * n), O (n2)
# SC: O(1), in-place.
def rotate1(nums, k):
    # determine how many k cycles, num cycles is the remainder of the length
    # of the array by modulo of rotations k
    if k > len(nums):
        k = len(nums) % k

    # for every rotation cycle
    for i in range(k):
        # store the last element in the array for use in next loop
        prev = nums[-1]
        # shift every element for the length of the array one space
        for j in range(len(nums)):
            # temp holds the original value of j
            temp = nums[j]
            # replace j with previous
            nums[j] = prev
            # update previous with temp
            prev = temp


# Approach 2, Temporary Storage
# TC: O(n)
# SC: O(n) for temp. array
def rotate2(nums, k):
    # store each element at the i + k rotated location in a temporary array
    # with this approach we can use the original array for reference
    # similar to brute force, we need to modulo the i + k position

    n = len(nums)  # store length of array since it'll be used a few times
    arr = [None] * n  # empty array of size n

    # place all elements using original array as source
    for i in range(n):
        arr[(i + k) % n] = nums[i]

    # copy temp array elements back into original array
    nums[:] = arr


# Approach 3, Slice and Reverse
# To come up with this you have to recognize the pattern
def rotate3(nums, k):
    # In the rotated array, the numbers from index 0 to k are the last k
    # numbers of the original order.
    n = len(nums)
    nums[:] = nums[n - k:] + nums[: n - k]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    nums_expected = [5, 6, 7, 1, 2, 3, 4]
    k = 3

print("Original array")
print("Rotated array")
print(nums)
rotate3(nums, k)
print(nums)

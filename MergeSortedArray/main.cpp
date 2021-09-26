/*
 * Merge Sorted Array : You are given two integer arrays nums1 and nums2,
 * sorted in non-decreasing order, and two integers m and n, representing
 * the number of elements in nums1 and nums2 respectively.
 * Merge nums1 and nums2 into a single array sorted in non-decreasing order.
 * The final sorted array should not be returned by the function, but instead be
 * stored inside the array nums1. To accommodate this, nums1 has a length of
 * m + n,\where the first m elements denote the elements that should be
 * merged, and the\last n elements are set to 0 and should be ignored. nums2
 * has \a length of n.
 */

#include <iostream>
#include <vector>
#include <algorithm>
// Naive solution
// Append contents of nums2 to nums1 and sort with STL
// TC = O(NLogN)
void mergeN(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n)
{
    for(int i : nums2)
        nums1[i+m] = nums2[i];
    std::sort(std::begin(nums1), std::end(nums1));
}

int main() {

    return 0;
}

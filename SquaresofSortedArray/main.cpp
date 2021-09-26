// Given an integer array nums sorted in non-decreasing order, return an
// array of the squares of each number sorted in non-decreasing order.
// 1 <= nums.length <= 104
//-104 <= nums[i] <= 104

/*
 * Create a new vector squares to hold final result.
 * Iterator through given vector, push to new vector and square element.
 * Sort elements in new vector in ascending order.
 *      Use std::sort for O(logn) trival solution.
 *      Use ? for O(n) optimized solution.
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <cmath> // for pow

// Trivial solution std::sort is NlogN.
std::vector<int> sortedSquaresTrivial(std::vector<int>& nums) {
    std::vector<int> sortedSquared;
    sortedSquared.reserve(nums.size());
for (int num : nums)
    {
        sortedSquared.push_back(pow(num, 2));
    }
    std::sort(sortedSquared.begin(), sortedSquared.end());
    return sortedSquared;
}

/*
 * O(n) solution
 * Approach: Array is already in sorted order to start.
 * After the negative value is squared, it could be larger than the largest
 * positive square.
 * Check for this condition starting at the far left and far right of the
 * array.
 * Point to neighboring value and continue comparisions, filling new array.
 */
std::vector<int> sortedSquares(std::vector<int>& nums) {
    int n = nums.size(); // store array size for easy access
    int left = 0; // start of negative elements
    int right = n - 1; // end of positive elements
    std::vector<int> result(n); // holds sorted squared array

    // iterate through array starting at end
    for (int i = n - 1; i >= 0; i--)
    {
        // negative squared is less than positive squared, assign to
        // vector at i
        if(std::abs(nums[left]) < std::abs(nums[right]))
        {
            result[i] = std::pow(nums[right], 2);
            right--; // shift right pointer left to next open space
        }
        // negative squared is greater than positive squared, assign to
        // vector at i
        else
        {
            result[i] = std::pow(nums[left], 2);
            left++; // shift left pointer right to next open space
        }
    }
    return result;
}

int main() {

    std::vector<int> nums = {-4, -1, 0, 3, 10};
    std::vector<int> sortedSqs = {0, 1, 9, 16, 100};

    if (sortedSquaresTrivial(nums) == sortedSqs)
        std::cout << "PASS\n";
    else
        std::cout << "FAIL\n";


    if (sortedSquares(nums) == sortedSqs)
        std::cout << "PASS\n";
    else
        std::cout << "FAIL\n";

    return 0;
}

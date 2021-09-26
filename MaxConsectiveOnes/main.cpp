// Given a binary array nums, return the maximum number of consecutive 1's in the array.
// 1 <= nums.length <= 105
// nums[i] is either 0 or 1.

/*
 * Approach:
 * Create var maximum to store the max consecutive 1s.
 * Create an index variable i for while loop control.
 * Run an outer while loop to run until vector end.
 * Check if current element is equal to 1. If not equal to one, continue.
 * If equal to 1, run nested while loop to track current count of consecutive
 * 1s with another accumulator variable. Traverse while equal to 1.
 * When 0 or end of array found, update maximum.
 * Return maximum after outer loop completes.
 */

#include <iostream>
#include <vector>

int findMaxConsecutiveOnes(std::vector<int>& nums)
{
    int maximum = 0;
    size_t i = 0; // outer loop control var

    while (i < nums.size())
    {
        int ones = 0;
        if (nums.at(i) == 1)
        {
            while(i < nums.size() && nums.at(i) == 1)
            {
                ones++;
                i++;
            }
        }
        maximum = std::max(maximum, ones);
        i++;
    }

    return maximum;
}

int main() {
    std::vector<int> nums = {1, 1, 0, 1, 1, 1};
    int maxConOnes = 3;
    if (findMaxConsecutiveOnes(nums) == maxConOnes)
        std::cout << "PASS\n";
    else
        std::cout << "FAIL\n";

    return 0;
}

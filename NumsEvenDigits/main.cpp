// Given an array nums of integers, return how many of them contain an even number of digits.
//1 <= nums.length <= 500
//1 <= nums[i] <= 10^5

/*
 * Initialize accumulator var totEven.
 * Iterate through vector. Initialize accumulator digitCount. At each element:
 *      Store num digits in digitCount.
 *      If even, increase totEven.
 *      Continue through vector.
 */

#include <iostream>
#include <vector>
#include <iterator>
#include <string>

int findNumbers(std::vector<int>& nums) {
    int totEven = 0;
    std::vector<int>::iterator it;
    for (it = nums.begin(); it != nums.end(); it++)
    {
        // Get number of digits from string operator length
        int digitCount = std::to_string(*it).length();
        if (digitCount % 2 == 0)
            totEven++;
    }
    return totEven;
}

int main() {
    std::vector<int>nums = {12, 345 ,2 ,6 ,7896};
    int numEven = 2;

    if (findNumbers(nums) == numEven)
        std::cout << "PASS\n";
    else
        std::cout << "FAIL\n";

    return 0;
}

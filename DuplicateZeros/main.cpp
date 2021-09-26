/*
 * Duplicate Zeros: Given a fixed-length integer array arr, duplicate each
 * occurrence of zero, shifting the remaining elements to the right.
 * Note that elements beyond the length of the original array are not written.
 * Do the above modifications to the input array in place and do not return
 * anything.
 */

/*
 * Optimal Approach: Because the size must stay the same, we trim from the end
 * everytime we insert.
 * Edge cases:
 *      arr.size() = 0, break
 */

#include <iostream>
#include <vector>

void duplicateZeros(std::vector<int>& arr)
{
    int n = arr.size();

    if (n == 0) // edge case
        return;

    for (int i = 0; i < n; i++)
    {
        if (arr.at(i) == 0)
        {
            arr.insert(arr.begin() + i + 1, 0);
            arr.pop_back(); // remove last element
            i++; // advance ptr again to skip added 0
        }
    }
}


int main() {
    std::vector<int> arr = {1, 0, 2, 3, 0, 4, 5, 0};
    std::vector<int> arrDup = {1, 0, 0, 2, 3, 0, 0, 4};

    duplicateZeros(arr);

    if (arr == arrDup)
        std::cout << "PASS\n" << std::endl;
    else
        std::cout << "FAIL\n" << std::endl;

    return 0;
}

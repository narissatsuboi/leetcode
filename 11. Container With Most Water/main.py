"""
You are given an integer array height of length n. There are n vertical
lines drawn such that the two endpoints of the ith line are (i, 0) and
(i, height[i]).

Find two lines that together with the x-axis form a container,
uch that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



1 8 6 2 5 4 8 3 7  l   1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8  i   0 3 7 5 4 2 8 1


"""

def maxAreaBF(height):
    """
    BF solution with nested loops.
    TC O(n2) SC O(1)
    :param height: arr of heights
    :return: mArea maximum area found
    """

    mArea = -1

    for i in range(len(height)):
        for j in range(i+1, len(height)):
            htLeft, htRight = height[i], height[j]
            currArea = (min(htLeft, htRight) * abs(i - j))
            mArea = max(currArea, mArea)

    return mArea


def maxAreaExtraSpace(height):
    """
    Solution with 2 pointers and extra space.
    TC O(n) SC O(n)
    :param height: arr of heights
    :return: mArea maximum area found
    """

    pairs = []
    mArea = -1

    # fill pairs with [i, height[i]]
    for i, lineHt in enumerate(height):
        pairs.append([i, lineHt])

    print(pairs)

    # sort
    pairs.sort(key=lambda x:x[1])

    print(pairs)

    # init pair pointers
    pRight = len(height)-1
    pLeft = pRight - 1


    while pLeft >= 0:
        # store positions
        iRight = pairs[pRight][0]
        iLeft = pairs[pLeft][0]

        # store corresponding heights
        htRight = pairs[pRight][1]
        htLeft = pairs[pLeft][1]

        # calculate the area
        currArea = (min(htRight, htLeft) * abs(iRight-iLeft))
        # store the area
        mArea = max(mArea, currArea)

        # increment pointers left
        pRight = pLeft
        pLeft -= 1
    return mArea # max amount of water a container can store.

def maxArea(height):
    """
    Optimized olution with 2 pointers and no extra space.
    TC O(n) SC O(1)
    :param height: arr of heights
    :return: mArea maximum area found
    """
    left, right = 0, len(height) - 1
    mArea = -1

    # traverse heights from out to in
    while left < right:

        # calculate the area code
        currArea = (right - left) * min(height[left], height[right])
        mArea = max(mArea, currArea)

        left += 1
        right -= 1

    return mArea

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    height = [1,0,0,0,0,0,0,2,2]
    print(maxArea(height))



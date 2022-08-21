"""
You are given an array prices where prices[i] is the price of a
given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one
stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If
you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


prices = [7, 1, 5, 3, 6, 4]

          l  r              profit = -6
             l   r          profit = 4
             l   -->  r     profit = 5

"""

def maxProfitBF(prices):
    """
    BF sol'n w/ nested for loops
    TC O(n2) SC O(1)
    :param prices: list of prices
    :return: max profit
    """

    mProfit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            mProfit = max(mProfit, prices[j] - prices[i])

    return mProfit


def maxProfit(prices):
    """
    Optimized sol'n w/ two pointers
    TC O(n) SC O(1)
    :param prices: list of prices
    :return: max profit
    """

    mProfit = 0
    left, right = 0, 1

    while right < len(prices):
        # calc max profit at this position
        if prices[left] < prices[right]:
            mProfit = max(mProfit, prices[right] - prices[left])
        else:
            left = right
        right += 1
    return mProfit


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfitBF(prices))
    print(maxProfit(prices))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

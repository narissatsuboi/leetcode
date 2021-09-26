# Narissa Tsuboi
# 122. Best Time to Buy and Sell Stock II
# 8/15/21


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # When current price is greater than the previous days price, add to
    # profit accumulator
    # TC is O(n), iterates through list once.
    # SC is O(1), constant space used.

    profit = 0  # accumulator to hold gains from each transaction

    # iterate through day 1 through end of prices
    for i in range(1, len(prices)):
        # add gains when current days price is greater than previous days
        if prices[i] > prices[i - 1]:
            # profit is the difference between the two prices
            profit += prices[i] - prices[i - 1]
    return profit


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [1, 2, 3, 4, 5]
    prices3 = [7, 6, 4, 3, 1]

    assert maxProfit(prices1) == 7
    assert maxProfit(prices2) == 4
    assert maxProfit(prices3) == 0


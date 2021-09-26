class Solution(object):
    #SLOWER
    def insert1(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        # list is sorted but if it wasn't sort with lambda expression first

        result = []

        for i in range(len(intervals)):
            # Clean insertion in front of intervals (would occur first iteration)
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

                # Clean insertion at end of intervals
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # Handle cases where newInterval overlaps with existing interval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]

        # Add the stored newInterval to the list before returning result
        result.append(newInterval)

        return result

    # FASTER
    def insert2(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        i = 0  # from 0th to last interval stored in intervals
        start, end = 0, 1
        result = []
        n = len(intervals)

        while i < n and intervals[i][end] < newInterval[start]:
            result.append(intervals[
                              i])  # add untouched intervals to result during iteration
            i += 1

        # overlap found, merge
        while i < n and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start],
                                     newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1

        # add big overlapped interval to result (if exists) otherwise its just the original one
        result.append(newInterval)

        # add the remainig intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result



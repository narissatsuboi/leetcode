"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the n
on-overlapping intervals that cover all the intervals in the input.
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # handle intervals of len less than 2
        if len(intervals) < 2:
            return intervals

        merged_intervals = []

        # sort on start
        intervals.sort(key=lambda x: x[0])

        # store previous interval
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        # run through 1 -> end intervals
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            # merge if start of the current interval < the end of the stored
            # interval
            if curr_start <= prev_end:
                prev_end = max(prev_end, curr_end)
            # else no merged interval found, store current standalone interval
            else:
                merged_intervals.append([prev_start, prev_end])
                prev_start = curr_start
                prev_end = curr_end
        # add last interval to result
        merged_intervals.append([prev_start, prev_end])

        return merged_intervals


if __name__ == '__main__':
    intervals = [[8, 10], [2, 6], [15, 18], [1, 3]]
    # intervals = [[1,4],[5,6]]
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    merged = Solution.merge(Solution, intervals)
    merged.sort(key=lambda x: x[0])
    print(merged)



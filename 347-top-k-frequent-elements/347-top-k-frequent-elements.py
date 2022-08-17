class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}  # holds {num : frequency}
        
        # arr where indexes represent frequency and eles represent the nums that occur the num times as index
        # size of bucket is 1 plus len of nums, number of distinct possibilities 
        bucket = [[] for i in range(len(nums) + 1)]
        
        # populate dict
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        # match counts to indices of bucket 
        for n, c in count.items():
            bucket[c].append(n)
        
        # store result from highest to lowest (k)
        res = []
        for i in range(len(bucket)-1, 0, -1):  # start at the end of th bucket
            # access the elements with the index i while i != k
            for n in bucket[i]:
                res.append(n)  # append connents of bucket to the result 
                
                # stop when k is reached
                if len(res) == k:
                    return res
                
        
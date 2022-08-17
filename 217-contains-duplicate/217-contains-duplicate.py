class Solution:
    
      def containsDuplicate(self, nums):
        """
        Check the set of the list is the same len as the list. 
        Not as intuitive but simple and fast. 
        Time O(n), Space O(1).  

        :type nums: List[int]
        :rtype: bool
        :param nums: The list of ints
        :return: returns True if duplicate exists in nums
    
        """  
        
        len_nums = len(nums)
        len_set_nums = len(set(nums))
        areDuplicates = len_nums != len_set_nums
        
        return areDuplicates
    
    
#     def containsDuplicate(self, nums):
#         """
#         Manual hashtable. Simple. Time O(n), Space O(1).  

#         :type nums: List[int]
#         :rtype: bool
#         :param nums: The list of ints
#         :return: returns True if duplicate exists in nums
    
#         """
#         # init empty dict
#         hashNum = {}
#         # iterate over nums
#         for i in nums:
#             if i not in hashNum:
#                 hashNum[i] = 1
#             else:
#                 return True
#         return False
    
    
    
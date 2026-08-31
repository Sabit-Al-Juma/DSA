class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            Counts=nums.count(i)
            if Counts ==1:
                return i
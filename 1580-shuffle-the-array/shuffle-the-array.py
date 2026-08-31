class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        middle = len(nums)//2
        
        first_half = nums[:middle]
        last_half = nums[middle:]
        
        result=[]
        for i in range(n):
            result.append(first_half[i])
            result.append(last_half[i])

        return result
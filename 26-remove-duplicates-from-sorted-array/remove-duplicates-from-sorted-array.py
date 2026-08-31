class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result= []

        for i in nums:
            if i not in result:
                result.append(i)

        for i in range(len(result)):
            nums[i]=result[i]
        k= len(result)
        return k 
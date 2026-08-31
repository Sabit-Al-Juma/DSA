class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        total=0
        #
        for i in digits:
            total = total *10 + i

        total+=1
        result = []
        for i in str(total):
            result.append(int(i))
        return result


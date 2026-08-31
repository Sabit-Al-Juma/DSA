class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # result=[]
        # for i in range(len(candies)):
        #     # candies[i] = candies[i] + extraCandies
        #     if candies[i] + extraCandies >= max(candies):
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result
        result=[]
        maximum = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i]+extraCandies
            if candies[i]>=maximum:
                result.append(True)
            else:
                result.append(False)
        return result
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        str_dict= {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno','7':'pqrs',
                    '8':'tuv', '9':'wxyz'}

        result=['']
        total=''
        for i in digits:
            new_result=[]
            for j in result:
                for k in str_dict[i]:
                    new_result.append(j+k)
                    result=new_result
        return result
       
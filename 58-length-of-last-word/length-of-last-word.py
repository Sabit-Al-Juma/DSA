class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        remove_space = s.split()
        return len(remove_space[-1])
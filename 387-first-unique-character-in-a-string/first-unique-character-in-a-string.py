class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        frequency={}
        for ch in s:
            frequency[ch]=frequency.get(ch,0)+1
        for i,ch in enumerate(s):
            if frequency[ch]==1:
                return i
        return -1
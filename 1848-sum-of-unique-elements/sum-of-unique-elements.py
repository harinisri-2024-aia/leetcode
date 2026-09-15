class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency={}
        total=0
        for x in nums:
            frequency[x]=frequency.get(x,0)+1
        for x in frequency:
            if frequency[x]==1:
                total+=x
        return total
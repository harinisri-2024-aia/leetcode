class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            return x
        left=0
        right=x
        answer=0
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            if mid*mid<x:
                answer=mid
                left=mid+1
            else:
                right=mid-1
        return answer
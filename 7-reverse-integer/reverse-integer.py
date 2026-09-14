class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=-1 if x<0 else 1
        x=abs(x)
        reverse=0
        while x>0:
            digit=x%10
            reverse=reverse*10+digit
            x=x//10
        reverse=reverse*sign
        if reverse<-2**31 or reverse>2**31-1:
            return 0
        return reverse
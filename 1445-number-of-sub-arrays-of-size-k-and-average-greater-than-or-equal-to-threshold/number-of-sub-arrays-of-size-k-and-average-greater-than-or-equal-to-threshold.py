class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        n=len(arr)
        left=0
        count=0
        current_sum=0
        for right in range(n):
            current_sum+=arr[right]
            if right-left+1>k:
                current_sum-=arr[left]
                left+=1
            if right-left+1==k:
                if current_sum>=k*threshold:
                    count+=1
        return count
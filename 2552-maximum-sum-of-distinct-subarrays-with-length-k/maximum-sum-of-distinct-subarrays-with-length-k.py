class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n=len(nums)
        left=0
        max_sum=0
        current_sum=0
        freq={}
        for right in range(n):
            current_sum+=nums[right]
            freq[nums[right]]=freq.get(nums[right],0)+1
            if right-left+1>k:
                freq[nums[left]]-=1
                current_sum-=nums[left]
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1
            if right-left+1==k:
                if len(freq)==k:
                    max_sum=max(current_sum,max_sum)
        return max_sum
        
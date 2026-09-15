class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        frequency={}
        for x in arr:
            frequency[x]=frequency.get(x,0)+1
        occurrences=[]
        for x in frequency:
            occurrences.append(frequency[x])
        return len(occurrences)==len(set(occurrences))
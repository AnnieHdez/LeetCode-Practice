class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        n = len(citations)
        r = n-1
        citations.sort()
        
        if n==0:
            return 0
        
        if n==1:
            if citations[0] == 0:
                return 0
            else:
                return 1
        
        while l<=r:
            m = l+(r-l)//2
            
            if citations[m] == n - m:
                return n - m
            
            if citations[m] > n-m:
                r = m-1
                
            else:
                l = m+1
            
        return n - r -1
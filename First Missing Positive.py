class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i]<0:
                nums[i] = 0     
                
        for j in range(n):
            temp = nums[j]
            if temp<0:
                temp*=-1
            if temp<=n and temp!=0:
                pos = nums[temp-1]
                if pos>0:
                    nums[temp-1]*=-1
                elif pos == 0:
                    nums[temp-1]=-n
        for i in range(n):
            if nums[i]>=0:
                return (i+1)
                
        return (n+1)
            
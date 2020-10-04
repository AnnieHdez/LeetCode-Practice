class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        
        if n<1:
            return 0
        
        if nums[0]<k:
            dp[0] = (nums[0], 0)
        else:
            dp[0] = (1,1)
        
        for i in range(1,n):
            if nums[i]*dp[i-1][0]<k:
                dp[i] = (nums[i]*dp[i-1][0], dp[i-1][1])
            elif nums[i]>=k:
                dp[i] = (1, i+1)
            else:
                temp = 1
                for j in range(dp[i-1][1]+1,i+1):
                    temp*=nums[j-1]
                    if(((nums[i]*dp[i-1][0])//temp)<k):
                        dp[i] = ((nums[i]*dp[i-1][0])//temp, j)                        
                        break
        count = 0
        for i in range(0,n):
            if i - dp[i][1]>=0:
                count+=((i-dp[i][1])+1)
                        
                
        return count
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0]*n
        dp2 = [0]*n
        dp1[0] = dp2[0] = nums[0]
        
        for i in range(1,n):
            if nums[i] > 0:
                dp1[i] = max(nums[i], nums[i]*dp1[i-1])
                dp2[i] = min(nums[i], nums[i]*dp2[i-1])
            else:
                dp1[i] = max(nums[i], nums[i]*dp2[i-1])
                dp2[i] = min(nums[i], nums[i]*dp1[i-1])
            
        return max(dp1)
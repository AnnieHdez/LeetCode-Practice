class Solution:
    from collections import defaultdict
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        
        if n<=1:
            return nums
        
        dp = [0]*n

        dp[-1] = 1
        sol = defaultdict(list)
        sol[nums[-1]] = [nums[-1]]
        maximum = n-1

        for i in range(n-2, -1, -1):
            maxim = 0
            sol[nums[i]].append(nums[i])
            maxIndex = -1
            for j in range(i+1, n):
                if nums[j]%nums[i]==0:
                    if dp[j] > maxim:
                        maxim = dp[j]
                        maxIndex = j
            dp[i] = maxim + 1
            if dp[i] > dp[maximum]:
                maximum = i
            if maxIndex>=0:
                sol[nums[i]] += sol[nums[maxIndex]]

        return sol[nums[maximum]]
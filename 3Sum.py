class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        n = len(nums)
        nums.sort()
        
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = n-1
            while start < end:
                if nums[start]+nums[end] == -nums[i]:
                    sol.add((nums[i], nums[start], nums[end]))
                    start+=1
                    
                    while nums[start] == nums[start-1] and start < end:
                        start+=1
                        
                elif nums[start]+nums[end] < -nums[i]:
                    start+=1
                    
                else:
                    end-=1
                
        return sol
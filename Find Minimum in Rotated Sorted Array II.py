class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.BinSearch(nums,0, len(nums)-1)
        
    def BinSearch(self, nums, l, r):
        if l>=r:
            return nums[l]
        m = (l+r)//2

        if nums[m]>nums[r]:
            return self.BinSearch(nums, m+1, r)
        elif nums[m]<nums[r]:            
            return self.BinSearch(nums, l, m)
        else:
            return self.BinSearch(nums,l,r-1)
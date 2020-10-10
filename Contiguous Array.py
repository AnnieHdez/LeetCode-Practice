class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0 
        dic = {0:-1}
        n = len(nums)
        maxLenght = 0
        
        for i in range(n):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
                
            if count in dic:
                maxLenght = max(maxLenght, i - dic[count])
            else:
                dic[count] = i
        
        return maxLenght
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
            
        prices = [0]*n
        
        for i in range(n):
            prices[i] = gas[i]- cost[i]
        
        current = 0
        prices = prices + prices
        index= 0
        
        for i in range(2*n):
            current+=prices[i]
            if current<0:
                current = 0
                index = i+1
                
        if index>n:
            return -1
        
        else:
            return index
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        kad = self.kadane(A)
        n = len(A)
        found = False
            
        suma = 0
        for i in range(n):
            suma += A[i]
            if A[i]>0:
                found = True
            A[i] = -A[i]
        
        if not found:
            return kad
            
        invert = suma + self.kadane(A)
        
        return max(kad, invert)
        
    def kadane(self, A: List[int]) -> int:
        maxim = A[0]
        current = A[0]
        n = len(A)
        
        for i in range(1,n):
            current = max(current+A[i], A[i])
            maxim = max(current, maxim)
            
        return maxim
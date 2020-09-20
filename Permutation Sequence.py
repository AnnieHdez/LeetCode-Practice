class Solution:
    import math
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1,1,2,6,24,120,720,5040,40320,362880]
        solution = ""
        numbers = [i for i in range(1,n+1)]
        val = k
        
        for i in range(n-1):
            factorial = fact[n-(i+1)]
            current = math.ceil(val/factorial)
            val = val%factorial
            solution += str(numbers[current-1])
            numbers.pop(current-1)
        
        solution+=str(numbers[0])
        return solution
        
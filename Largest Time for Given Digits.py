class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        arr = list(permutations(sorted(A, reverse=True)))
        
        for h1, h2, m1, m2 in arr:
            if h1 * 10 + h2 < 24 and m1 * 10 + m2 < 60:
                return str(h1)+str(h2)+":"+str(m1)+str(m2)
        return ''
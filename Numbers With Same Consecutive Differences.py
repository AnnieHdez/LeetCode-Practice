class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        numbs = []
        
        if N==1:
            return range(10)
        
        for i in range(1, 10):
            if i+K<=9 or i-K>=0:
                numbs.append([i])
                
                
        for leng in range(1,N):
            answer = []
            for num in numbs:
                if num[leng-1]+K<=9:
                    answer.append(num+[num[leng-1]+K])
                
                if num[leng-1]-K>=0:
                    answer.append(num+[num[leng-1]-K])
                
            numbs = answer
        
        p = []
        for ans in answer:
            p.append(''.join(map(str, ans)))
        
        r = set(p)
        return r
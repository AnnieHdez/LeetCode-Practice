class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
    
        if n<1:
            return ugly[0]

        two = 2
        three = 3
        five = 5
        index2 = 0
        index3 = 0
        index5 = 0
        count = 0

        while count<=n:
            count+=1
            minimun = min(min(two, three),five)
            ugly.append(minimun)
            
            if minimun == two:
                index2 += 1
                two = ugly[index2]*2
            if minimun == three:
                index3 += 1
                three = ugly[index3]*3
            if minimun == five:
                index5 += 1 
                five = ugly[index5]*5                

        return ugly[n-1]
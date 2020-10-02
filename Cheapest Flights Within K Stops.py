class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = [[0]*n  for i in range(n)]
        
        for flight in flights:
            graph[flight[0]][flight[1]] = flight[2]
            
        q = [src]
        prices = [0]
        minPrices = [0]*n
        answer = 100000000000000
        
        while len(q)!=0 and K>=0:
            K-=1
            level = len(q)
            
            for i in range(level):
                current = q.pop(0)
                acumulativePrice = prices.pop(0)
                
                for j in range(n):
                    currentPrice = graph[current][j]
                    if currentPrice > 0:
                        actualPrice = acumulativePrice + currentPrice
                        minPrice = minPrices[j]
                        if minPrice == 0 or actualPrice < minPrice:
                            minPrices[j] = actualPrice
                            q.append(j)
                            prices.append(actualPrice)
                            if j == dst and answer > actualPrice:
                                answer = actualPrice
                                
        if answer == 100000000000000:
            return -1
        else:
            return answer
from collections import defaultdict
answer = []
dic = defaultdict(list)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.dic = defaultdict(list)
        tickets.sort(key=lambda x: x[1])
        for pair in tickets:
            self.dic[pair[0]].append(pair[1])        
        
        self.answer = []
        self.dfs("JFK")
        
        return self.answer[::-1]
    
    def dfs(self, city):
        while city in self.dic and len(self.dic[city]) > 0:
            nxt = self.dic[city][0]
            (self.dic[city]).pop(0)
            self.dfs(nxt)
        
        self.answer.append(city)            
        return answer
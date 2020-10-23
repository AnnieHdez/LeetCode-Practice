class Solution:
    def compare(self, s, p):
        for i in range(26):
            if s[i]!=p[i]:
                return False      
        return True
    
    def findAnagrams(self, s: str, p: str):
        pattern = [0]*26
        word = [0]*26
        index = []
        n = len(p)
        ns = len(s)
        
        if n>ns or (n==0 or ns==0):
            return index
        
        for i in range(n):
            pattern[ord(p[i]) - 97] += 1
            word[ord(s[i]) - 97] += 1
        
        for i in range(n, ns):
            if self.compare(pattern, word):
                index.append(i-n)
            word[ord(s[i])-97]+=1
            word[ord(s[i-n])-97]-=1
        if self.compare(pattern, word):
            index.append(ns-n)                     
        return index
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        caws = 0
        n = len(secret)
        s={}
        g={}
        
        for i in range(n):
            if secret[i] in s:
                s[secret[i]]+=1
            else:
                s[secret[i]] = 1
            if guess[i] in g:
                g[guess[i]]+=1
            else:
                g[guess[i]] = 1
        
        for i in range(n):
            if secret[i] == guess[i]:
                bulls+=1
                s[guess[i]]-=1
                g[guess[i]]-=1
                
        for i in range(n):
            if guess[i] in secret:
                if s[guess[i]]>0 and g[guess[i]]>0:
                    s[guess[i]]-=1
                    g[guess[i]]-=1
                    caws+=1
                    
        return (str(bulls) + "A" + str(caws) + "B")
        
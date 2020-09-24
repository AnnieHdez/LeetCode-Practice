class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        found = False
        if k>=len(num):
            return "0"
        i = 0

        while i<len(num)-1:
            if num[i]>num[i+1]:
                num=num[:i]+num[i+1:]
                k-=1
                if k==0:
                    break
                if i>0:
                    i-=1
                    while num[i]>num[i+1]:
                        num=num[:i]+num[i+1:]
                        k-=1
                        if i==0:
                            break
                        if k==0:
                            found = True
                            break
                        i-=1
                if found:
                    break
                else:
                    i-=1
            i+=1

        if k>0:
            num = num[:len(num)-k]

        i = 0
    
        while i<len(num):
            if num[i]=='0' and len(num)>1:
                num =  num[i+1:]
            else:
                break


        return num
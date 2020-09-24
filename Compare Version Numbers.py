class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        n = len(ver1)
        m = len(ver2)
        
        for i in range(min(n,m)):
            if int(ver1[i])>int(ver2[i]):
                return 1
            elif int(ver2[i])>int(ver1[i]):
                return -1
            
        if m>n:
            for i in range(n,m):
                if int(ver2[i])>0:
                    return -1     
        
        if n>m:
            for i in range(m,n):
                if int(ver1[i])>0:
                    return 1               
                
        return 0
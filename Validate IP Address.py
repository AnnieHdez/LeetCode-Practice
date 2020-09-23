import ipaddress

class Solution:
    def ipv4(self, l):
        for i in l:
            if not i.isdigit() or (len(i)>1 and i[0]=='0') or int(i)>255:
                return False
            
        else:
            return True


    def ipv6(self, s):       
        try:
            ipaddress.IPv6Network(s)        
            return True
        except ValueError:
            return False
    
    def validIPAddress(self, IP: str) -> str:       
        l=IP.split(".")
        if len(l)==4 and self.ipv4(l):
            return "IPv4"
        
        l=IP.split(":")    
        if len(l)==8:
            for i in l:
                if len(i)<1:
                    return "Neither"
                
            if[l[0][0]!="0"] and self.ipv6(IP):
                    return "IPv6"
        
        return "Neither"
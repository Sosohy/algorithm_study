import re
from collections import Counter

def solution(str1, str2):
    answer = 0
    str1, str2 = str1.upper(), str2.upper()
    l1 = []
    l2 = []
    
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if(tmp.isalpha()):
            l1.append(str1[i:i+2])
        
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if(tmp.isalpha()):
            l2.append(str2[i:i+2])
    
    c1 = Counter(l1)
    c2 = Counter(l2)
    
    inter = (c1 & c2).values()
    union = (c1 | c2).values()
    
    if(not inter) and (not union):
        return 65536
    
    answer = int(sum(inter)/sum(union) * 65536)
    
    return answer
    
    
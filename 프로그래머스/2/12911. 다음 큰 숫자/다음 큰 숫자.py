def solution(n):
    answer = 0
    nBin = bin(n)[2:].count("1")
    num = n+1
    
    while(True):
        tmpBin = bin(num)[2:].count("1")
        
        if(nBin == tmpBin):
            answer = num
            break
        else:
            num += 1
    
    return answer
def getNtext(n, end):
    numText= "0"
    idx = 1
    dic = {10 : 'A', 11: "B", 12: 'C', 13: 'D', 14:'E', 15: 'F'}
    
    while len(numText) <= end:
        tmp = ''
        tIdx = idx
        while(tIdx > 0):
            if(tIdx%n >= 10):
                tmp += dic[tIdx%n]
            else:
                tmp += str(tIdx%n)
            tIdx = tIdx//n
        numText += tmp[::-1]
        idx += 1
        
    return numText

def solution(n, t, m, p):
    answer = ''
    numText = getNtext(n, m*t)
    
    for i in range(t):
        idx = p + (m*i)
        answer += numText[idx-1]
    
    return answer
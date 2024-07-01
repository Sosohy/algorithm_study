def solution(s):
    answer = 0

    x = 0
    notX = 0
    idx = 0
    
    for i in range(len(s)):
        if(x == notX):
            idx = i
            x, notX = 0, 0
            answer += 1
            
        if(s[i] == s[idx]):
            x += 1
        else:
            notX += 1
            
    return answer
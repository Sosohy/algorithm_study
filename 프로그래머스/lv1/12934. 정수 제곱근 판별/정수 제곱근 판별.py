def solution(n):
    answer = -1
    s = n**0.5
    
    if s == int(s):
        answer = (s + 1) ** 2
    
    return answer
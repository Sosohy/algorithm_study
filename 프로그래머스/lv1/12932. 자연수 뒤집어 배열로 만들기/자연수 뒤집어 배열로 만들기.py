def solution(n):
    answer = []
    n = str(n)
    
    for i in range(1, len(n)+1):
        answer.append(int(n[-1*i]))
    
    return answer # list(map(int, reversed(str(n))))
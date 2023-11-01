def solution(hp):
    answer = 0
    ant = [5, 3, 1]
    
    for i in range(3):
        answer += hp//ant[i]
        hp = hp%ant[i]
    
    return answer
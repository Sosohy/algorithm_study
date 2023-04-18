def solution(price, money, count):
    answer = 0
    
    for i in range(count):
        answer += price*(i+1)

    answer -= money 
    
    return max(0, answer)
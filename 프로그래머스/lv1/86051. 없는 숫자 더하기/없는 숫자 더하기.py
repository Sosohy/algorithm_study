def solution(numbers):
    answer = [x for x in range(10)]
    
    for i in numbers:
        answer.remove(i)
            
    return sum(answer)
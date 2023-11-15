def solution(array, commands):
    answer = []
    
    for i in commands:
        s, e, k = i
        tmpList = array[s-1:e]
        answer.append(sorted(tmpList)[k-1])
    
    return answer
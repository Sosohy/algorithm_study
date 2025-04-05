def solution(ingredient):
    answer = 0
    
    if(len(ingredient) < 4): return 0

    ham = ingredient[:3]
    
    for i in range(3, len(ingredient)):
        ham.append(ingredient[i])
        if(ham[-4:] == [1, 2, 3, 1]):
            answer += 1
            del ham[-4:]
    
    return answer
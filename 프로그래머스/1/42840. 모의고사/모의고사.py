def solution(answers):
    answer = [0, 0, 0]
    
    one = "12345"
    two = "21232425"
    three = "3311224455"
    
    for i in range(len(answers)):
        if(int(one[i%len(one)]) == answers[i]): answer[0] += 1
        
        if(int(two[i%len(two)]) == answers[i]): answer[1] += 1
        
        if(int(three[i%len(three)]) == answers[i]): answer[2] += 1

    p = []
    for i in range(3):
        if max(answer) == answer[i]:
            p.append(i+1)
        
    return p
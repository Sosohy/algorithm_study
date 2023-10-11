def solution(X, Y):
    answer = ''
    
    for i in set(X)&set(Y):
        tmp = min(X.count(i), Y.count(i))
        answer += i*tmp

    if(not answer): 
        return "-1"
    elif(answer.count('0') == len(answer)):
        return "0"
    else:
        answer = ''.join(sorted(answer, reverse=True))

    return answer

'''
def solution(X, Y):
    answer = ''
    
    for i in X:
        if(i not in answer) and (i in Y):
            tmp = min(X.count(i), Y.count(i))
            answer += i*tmp

    if(not answer): 
        return "-1"
    elif(answer.count('0') == len(answer)):
        return "0"
    else:
        answer = ''.join(sorted(answer, reverse=True))

    return answer
'''
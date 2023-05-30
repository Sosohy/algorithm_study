def solution(s):
    answer = True
    sList = []
    
    for i in s:
        if i == '(':
            sList.append(i)
        else:
            if(sList):
                sList.pop()
            else:
                return False
                
    if (sList):
        answer = False

    return answer
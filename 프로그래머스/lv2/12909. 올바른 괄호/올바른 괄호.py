def solution(s):
    answer = True
    sList = []
    
    for i in s:
        if i == '(':
            sList.append(i)
        else:
            if not sList:
                return False
            else:
                sList.pop()
                
    if (sList):
        answer = False

    return answer
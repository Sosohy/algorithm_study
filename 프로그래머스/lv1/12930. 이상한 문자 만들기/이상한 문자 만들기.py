def solution(s):
    answer = []
    sList = s.split(' ')
    
    for i in sList:
        sTmp = ""
        for j in range(len(i)):
            if(j%2 == 0):
                sTmp += i[j].upper()
            else:
                sTmp += i[j].lower()
        answer.append(sTmp)
    
    return ' '.join(answer)
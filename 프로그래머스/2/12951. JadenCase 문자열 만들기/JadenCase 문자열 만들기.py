def solution(s):
    answer = []
    sList = s.split(" ")
    
    for i in sList:
        if(i):
            tmp = i[0].upper() + str(i[1:]).lower()
            answer.append(tmp)
        else:
            answer.append(i)

    return " ".join(answer)


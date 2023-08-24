def solution(s):
    answer = []
    s = s[2:-2]
    sList = s.split('},{')
    sList.sort(key=len)
    
    for i in sList:
        tmp = i.split(',')
        for j in tmp:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer
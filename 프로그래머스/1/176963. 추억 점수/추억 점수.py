def solution(name, yearning, photo):
    answer = []
    score = {}
    
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    for i in photo:
        cnt = 0
        for j in i:
            if(j in score):
                cnt += score[j]
        answer.append(cnt)
    
    return answer
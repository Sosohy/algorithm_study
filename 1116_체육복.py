import copy
def solution(n, lost, reserve):
    reserve.sort()
    lost.sort()
    lostC = copy.deepcopy(lost)
    
    for i in lostC: #도난 학생이 여벌 체육복 가져온 학생
        if i in reserve:
            reserve.remove(i) 
            lost.remove(i)
    
    for i in reserve: #도난 학생이 다른 학생의 체육복 빌릴때
        if (i-1) in lost:
            lost.remove(i-1)
        elif (i+1) in lost:
            lost.remove(i+1)
    
    answer = n - len(lost) 
    return answer
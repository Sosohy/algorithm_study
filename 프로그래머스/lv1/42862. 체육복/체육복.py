import copy
def solution(n, lost, reserve):
    reserve.sort()
    lost.sort()
    lostC = copy.deepcopy(lost)
    
    for i in lostC: #도난 학생이 여벌 체육복 가져온 학생
        if i in reserve: 
            reserve.remove(i) # 여벌 학생 리스트에서 제거
            lost.remove(i) # 잃어버린 학생 리스트에서 제거
    
    for i in reserve: #도난 학생이 다른 학생의 체육복 빌릴때
        if (i-1) in lost: # 앞 번호 학생이 도난 학생일 경우
            lost.remove(i-1)
        elif (i+1) in lost: # 뒷 번호 학생이 도난 학생일 경우
            lost.remove(i+1)
    
    answer = n - len(lost) # 전체 학생 - 최종 체육복 없는 학생
    return answer
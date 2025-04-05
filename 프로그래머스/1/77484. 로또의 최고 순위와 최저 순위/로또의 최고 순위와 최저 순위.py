def solution(lottos, win_nums):
    answer = []
    
    minNum = len(set(win_nums) & set(lottos))
    maxNum = minNum + lottos.count(0)
    
    answer.append(min(6, 7-maxNum))
    answer.append(min(6, 7-minNum))
    
    return answer
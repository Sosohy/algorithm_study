def solution(lottos, win_nums):
    answer = []
    minNum = 0;
    
    for lotto in lottos:
        if lotto in win_nums:
            minNum += 1

    maxNum = minNum + lottos.count(0)
    
    answer.insert(0, ((7-maxNum) if (7-maxNum < 6) else 6))
    answer.insert(1, ((7-minNum) if (7-minNum < 6) else 6))
    
    return answer


'''
# 첫 번째 방법
def solution(lottos, win_nums):
    answer = []
    
    minNum = len(set(lottos) & set(win_nums))
    maxNum = minNum + lottos.count(0)
    
    answer.insert(0, ((7-maxNum) if (7-maxNum < 6) else 6))
    answer.insert(1, ((7-minNum) if (7-minNum < 6) else 6))
    
    return answer
'''
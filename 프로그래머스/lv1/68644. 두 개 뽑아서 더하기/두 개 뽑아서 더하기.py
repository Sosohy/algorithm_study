def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                answer.append(numbers[i] + numbers[j])

    answer = list(set(answer))
    
    return sorted(answer)

    '''
    # 다르게 짜본 코드 - combinations 이용
    
    from itertools import combinations
    
    combList = list(set(combinations(numbers, 2))) # 조합 만들기 / 중복 제거
    
    for x, y in combList:
        answer.append(x+y)
    
    answer = list(set(answer))
    '''



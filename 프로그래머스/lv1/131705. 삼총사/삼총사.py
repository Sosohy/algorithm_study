from itertools import combinations

def solution(number):
    answer = 0
    
    combList = list(combinations(number, 3))
    
    for i in combList:
        if sum(i) == 0:
            answer += 1
    
    return answer

'''
def solution(number):
    answer = 0
    
    for i in range(0, len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                num = [number[i], number[j], number[k]]
                if sum(num) == 0:
                    answer += 1
        
    return answer
'''


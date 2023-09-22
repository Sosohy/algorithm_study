answer = 0
def DFS(i, result, numbers, target):
    global answer
    
    if i == len(numbers):
        if result == target:
            answer += 1
        return
    else:
        DFS(i+1, result+numbers[i], numbers, target)
        DFS(i+1, result-numbers[i], numbers, target)
        
def solution(numbers, target):
    DFS(0, 0, numbers, target)
    
    return answer

'''
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((numbers[0], 0))
    queue.append((-1*numbers[0], 0))
    
    while queue:
        num, i = queue.popleft()
        
        if i+1 < len(numbers):
            queue.append((num+numbers[i+1], i+1))
            queue.append((num-numbers[i+1], i+1))
        else:
            if num == target:
                answer += 1
    
    return answer
'''
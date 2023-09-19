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


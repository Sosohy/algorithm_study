def solution(numbers, target):
    answer = 0
    visited = [0]*len(numbers)
    
    def dfs(i, s, target):
        nonlocal answer
        
        if(i >= len(numbers)):
            if(s == target):
                answer += 1
            return
        else:
            visited[i] = 1
            dfs(i+1, s+numbers[i], target)
            dfs(i+1, s-numbers[i], target)
    
    dfs(0, 0, target)
    
    return answer
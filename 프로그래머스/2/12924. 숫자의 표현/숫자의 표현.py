def solution(n):
    answer = 0
    
    for i in range(n):
        sum = 0
        for j in range(i+1, n+1):
            sum += j
            if(sum > n): break
            if(sum == n):
                answer += 1
                break

    return answer
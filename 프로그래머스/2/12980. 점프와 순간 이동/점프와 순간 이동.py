def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            ans += 1
    return ans

# 효율성 테스트X
# def solution(n):
#     dp = [0]*(n+1)
#     dp[0] = 0
#     dp[1] = 1
    
#     for i in range(2, n+1):
#         if i % 2 == 0:
#             dp[i] = dp[i//2]
#         else:  # 홀수
#             dp[i] = dp[i//2] + 1
    
#     return dp[n]
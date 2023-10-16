def solution(n):
    dp = [0 for i in range(n+1)]
    dp[2] = 3
    dp[4] = 11
    
    if n%2 != 0:
        return 0
    elif n <= 4:
        return dp[n]
    
    for i in range(6, n+1, 2):
        dp[i] = (3*dp[i-2] + sum(dp[2:i-3])*2 + 2)%1000000007
    
    '''
    for i in range(6, n+1, 2):
        dp[i] = (dp[i-2]*4+dp[i-4])%1000000007
        
    for i in range(3, index+1):
    	# answer[i:j] -> answer에서 index가 i인 원소부터 j-1인 원소까지의 sub-array
        answer.append((3*answer[i-1]+sum(answer[1:i-1])*2+2)%1000000007)
    '''
    return dp[n]
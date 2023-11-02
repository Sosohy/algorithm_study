def solution(N, number):
    if N == number:
        return 1
    answer = -1
    dp = [set([N])]
    
    for i in range(2, 9):
        nSet = set([int(str(N)*i)])
        for j in range(1, i):
            for n1 in dp[j-1]:
                for n2 in dp[i-j-1]:
                    nSet.add(n1+n2)
                    nSet.add(n1-n2)
                    nSet.add(n1*n2)
                    if(n2 != 0): nSet.add(n1//n2)
        if number in nSet:
            return i
        dp.append(nSet)

    return answer
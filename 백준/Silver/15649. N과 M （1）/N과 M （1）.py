n, m = map(int, input().split())
checkList = [0]*(n+1)
answer = []

def dfs(num):
    if(num == m):
        print(' '.join(map(str, answer)))
        return
    
    for i in range(1, n+1):
        if(checkList[i] == 0):
            answer.append(i)
            checkList[i] = 1
            dfs(num+1)
            answer.pop()
            checkList[i] = 0

dfs(0)
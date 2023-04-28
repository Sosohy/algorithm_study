# 2847: 게임을 만든 동준이

n = int(input())
score = [int(input()) for i in range(n)]
score.reverse()
ans = 0

for i in range(1, len(score)):
    if(score[i-1] <= score[i]):
        r = score[i] - (score[i-1]-1)
        score[i] -= r
        ans += r
        
print(ans)

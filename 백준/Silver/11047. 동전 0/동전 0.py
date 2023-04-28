n, k = map(int, input().split())
coins = [int(input()) for x in range(n)]
coins.sort(reverse=True)

ans = 0

for i in coins:
    if(k%i != k):
        ans += k//i
        k = k%i
        
    if(k == 0):
        break

print(ans)

n, k = map(int, input().split())
coinList = [int(input()) for i in range(n)]

cnt = 0

coinList.sort(reverse = True)

for i in coinList:
    cnt += k//i
    k = k%i

print(cnt)
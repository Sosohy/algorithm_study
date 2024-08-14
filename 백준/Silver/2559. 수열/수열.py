n, k = map(int, input().split())
tempList = list(map(int, input().split()))

sumList = sum(tempList[:k])
answer = sumList

s, e = 0, k

for i in range(k, n):
    sumList = sumList - tempList[s] + tempList[e]
    answer = max(answer, sumList)
    s += 1
    e += 1

print(answer)
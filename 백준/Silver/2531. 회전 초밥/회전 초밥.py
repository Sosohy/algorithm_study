n, d, k, c = map(int, input().split())
sList = []

for i in range(n):
    sList.append(int(input()))

eat = sList[:k]
tmp = set(eat)
tmp.add(c)

answer = len(tmp)

s, e = 0, k

for i in range(n):
    eat.pop(0)
    eat.append(sList[e])

    tmp2 = set(eat)
    tmp2.add(c)
    answer = max(answer, len(tmp2))
    
    e = (e+1)%n

print(answer)


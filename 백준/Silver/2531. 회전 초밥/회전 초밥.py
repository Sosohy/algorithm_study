n, d, k, c = map(int, input().split())
sList = []

for i in range(n):
    sList.append(int(input()))

eat = sList[:k]
types = set(eat)
types.add(c)

answer = len(types)

for i in range(n):
    eat.pop(0)
    eat.append(sList[(k+i)%n])

    types = set(eat)
    types.add(c)
    answer = max(answer, len(types))

print(answer)

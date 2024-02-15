n = int(input())
person = list()
rank = [1]*n

for i in range(n):
    weight, height = map(int, input().split())
    person.append((weight, height))

for i in range(n):
    p = person[i]
    for j in range(n):
        other = person[j]
        if(j != i and p[0] < other[0] and p[1] < other[1]):
            rank[i] += 1

for i in rank:
    print(i, end=" ")
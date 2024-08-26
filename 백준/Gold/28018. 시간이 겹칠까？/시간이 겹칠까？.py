import itertools

n = int(input())
nList = [0]*1000002

for i in range(n):
    s, e = map(int, input().split())
    nList[s] += 1
    nList[e+1] -= 1

ac = list(itertools.accumulate(nList))

m = int(input())
mList = list(map(int, input().split()))

for i in mList:
    print(ac[i])

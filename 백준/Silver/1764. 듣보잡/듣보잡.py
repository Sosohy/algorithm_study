N, M = map(int, input().split())

nList = [input() for i in range(N)]
mList = [input() for i in range(M)]

nList.sort()
mList.sort()
ans = [] 

def search(s, e, m):
    mid = 0
    while(s <= e):
        mid = (s+e)//2
        if(nList[mid] == m):
            ans.append(m)
        if(nList[mid] < m):
            s = mid+1
        else:
            e = mid-1

for m in mList:
    search(0, N-1, m)

print(len(ans))
for i in ans:
    print(i)

n = int(input())
nList = list(map(int, input().split()))

m = int(input())
isExistList = list(map(int, input().split()))

def bs(s, e, target):
    if(s == e):
        if(isExistList[target] == nList[s]):
            isExistList[target] = 1
        else:
            isExistList[target] = 0
        return
    
    mid = (s+e)//2
    if(nList[mid] < isExistList[target]):
        bs(mid+1, e, target)
    else:
        bs(s, mid, target)

nList.sort()
for i in range(m):
    bs(0, n-1, i)

for i in isExistList:
    print(i)

N, M = map(int, input().split())
treeList = list(map(int, input().split()))

treeList.sort()

l, r, mid = 1, treeList[-1], 0

while(l <= r):
    mid = (l+r)//2
    
    s = 0
    for tree in treeList:
        if(mid < tree):
            s += tree-mid
        
    if s >= M:
        l = mid+1
    else:
        r = mid-1

print(r)
n, m = map(int, input().split())

selected = [0 for i in range(m)]
def pert(nList, idx):
    if(idx >= m):
        pList = list(map(str, nList))
        p = " ".join(pList)
        print(p)
    else:
        for i in range(1, n+1):
            nList[idx] = i
            pert(nList, idx+1)
            nList[idx] = 0

pert(selected, 0)
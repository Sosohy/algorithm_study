n, m = map(int, input().split())
nList = sorted(list(map(int, input().split())))

perList = [0]*m
used = [0]*n
pList = set()

def per(idx):
    if(idx == m):
        tmp = " ".join(list(map(str, perList)))
        if(tmp not in pList):
            print(tmp)
            pList.add(tmp)
    else:
        for i in range(n):
            if(used[i] == 0):
                perList[idx] = nList[i]
                used[i] = 1
                per(idx+1)
                perList[idx] = 0
                used[i] = 0

per(0)
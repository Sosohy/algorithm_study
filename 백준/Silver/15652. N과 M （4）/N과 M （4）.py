n, m = map(int, input().split())

selected = [0 for i in range(m)]

def per(nList, idx):
    if(idx >= m):
        print(" ".join(list(map(str, nList))))
    else:
        for i in range(1, n+1):
            if(idx == 0):
                nList[idx] = i
                per(nList, idx+1)
                nList[idx] = 0
            elif(nList[idx-1] <= i):
                nList[idx] = i
                per(nList, idx+1)
                nList[idx] = 0

per(selected, 0)
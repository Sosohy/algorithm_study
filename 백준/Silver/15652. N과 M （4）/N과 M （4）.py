n, m = map(int, input().split())

selected = [0 for i in range(m)]

def per(nList, idx):
    if(idx >= m):
        print(" ".join(list(map(str, nList))))
    else:
        s = 1 if idx == 0 else nList[idx-1]
        for i in range(s, n+1):
            nList[idx] = i
            per(nList, idx+1)
            nList[idx] = 0

per(selected, 0)
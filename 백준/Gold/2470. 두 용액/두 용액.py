N = int(input())
nList = list(map(int, input().split()))

nList.sort()

idx = (0, N-1)
tmpIdx = [0, N-1]
minSum = abs(nList[idx[0]] + nList[idx[1]])

while(tmpIdx[0] < tmpIdx[1]):
    s = nList[tmpIdx[0]] + nList[tmpIdx[1]]

    if(abs(s) < minSum):
        idx = (tmpIdx[0], tmpIdx[1])
        minSum = abs(s)
    
    if(s <= 0):
        tmpIdx[0] += 1
    else:
        tmpIdx[1] -= 1

print(nList[idx[0]], nList[idx[1]])

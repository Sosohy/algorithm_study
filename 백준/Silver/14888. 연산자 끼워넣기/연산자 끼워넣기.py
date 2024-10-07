n = int(input())
nList = list(map(int, input().split()))
opList = list(map(int, input().split()))

result = []

def cal(v1, op, v2):
    if(op == 0): # +
        return v1 + v2
    elif(op == 1): # -
        return v1 - v2
    elif(op == 2): # *
        return v1 * v2
    else: # //
        if(v1 < 0):
            return -((-v1)//v2)
        else:
            return v1 // v2

def per(value, idx):
    if(idx >= n-1):
        result.append(value)
    else:
        for i in range(len(opList)):
            if(opList[i] > 0):
                opList[i] -= 1
                per(cal(value, i, nList[idx+1]), idx+1)
                opList[i] += 1

per(nList[0], 0)
print(max(result))
print(min(result))

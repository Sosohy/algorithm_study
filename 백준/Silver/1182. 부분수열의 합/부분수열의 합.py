n, s = map(int, input().split())
nList = list(map(int, input().split()))
answer = 0

def addNum(idx, value):
    global answer

    if(idx == n):
        if(value == s):
            answer += 1
            return
    else:
        addNum(idx+1, value + nList[idx])
        addNum(idx+1, value)

addNum(0, 0)
if(s == 0):
    answer -= 1
print(answer)


answer = 0
h, w = map(int, input().split())
blocks = list(map(int, input().split()))

lp, rp = 0, len(blocks)-1
m = blocks.index(max(blocks)) 

# 왼쪽
for i in range(0, m + 1):
    if blocks[lp] > blocks[i]:
        answer += (blocks[lp] - blocks[i])
    elif blocks[lp] <= blocks[i]:
        lp = i

# 오른쪽
for i in range(rp, m, -1):
    if blocks[rp] > blocks[i]:
        answer += (blocks[rp] - blocks[i])
    elif blocks[rp] <= blocks[i]:
        rp = i

print(answer)
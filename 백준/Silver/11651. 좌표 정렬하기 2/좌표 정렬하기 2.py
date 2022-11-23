import sys
ans = []

n = int(sys.stdin.readline())
for i in range(n):
	x, y = map(int, input().split())
	ans.append((x, y))

ans.sort(key = lambda x:(x[1], x[0]))

for i in ans:
    print(i[0], i[1])
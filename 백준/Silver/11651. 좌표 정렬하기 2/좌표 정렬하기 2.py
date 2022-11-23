import sys

n = int(sys.stdin.readline())
dot = [list(map(int, input().split())) for x in range(n)]

dot.sort(key = lambda x:(x[1], x[0]))

for (x, y) in dot:
    print(x, y)

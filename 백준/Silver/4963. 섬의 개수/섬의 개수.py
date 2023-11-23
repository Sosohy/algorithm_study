from collections import deque

while (True):
    w, h = map(int, input().split())
    if w == 0 and h == 0: break

    mList = []
    for i in range(h):
        mList.append(list(map(int, input().split())))


    def bfs(i, j):
        q = deque()
        q.append((i, j))
        pos = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        mList[i][j] = 2

        while (q):
            x, y = q.popleft()

            for k in range(8):
                nx = x + pos[k][0]
                ny = y + pos[k][1]

                if (0 <= nx < h and 0 <= ny < w) and mList[nx][ny] == 1:
                    q.append((nx, ny))
                    mList[nx][ny] = 2


    island = 0
    for i in range(h):
        for j in range(w):
            if (mList[i][j] == 1):
                bfs(i, j)
                island += 1

    print(island)
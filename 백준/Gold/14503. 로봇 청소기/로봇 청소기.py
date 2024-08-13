n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = []

pos = {0: (-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
answer = 0

for i in range(n):
    room.append(list(map(int, input().split())))

while((0 <= x < n) and (0 <= y < m) and room[x][y] != 1):
    if(room[x][y] == 0):
        answer += 1
        room[x][y] = 2
    
    for i in range(4):
        p = pos[(d + 3 - i) % 4]
        nx = x + p[0]
        ny = y + p[1]
        if((0 <= nx < n) and (0 <= ny < m) and room[nx][ny] == 0):
            x, y = nx, ny
            d = (d + 3 - i) % 4
            break
    else:
        x += pos[d][0] * -1
        y += pos[d][1] * -1

print(answer)
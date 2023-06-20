from itertools import combinations 

n, m = map(int, input().split())
cityMap = []

for i in range(n):
    r = list(map(int, input().split()))
    cityMap.append(r)

#print(cityMap)
house = []
chicken = []
answer = -1

for i in range(n):
    for j in range(n):
        if cityMap[i][j] == 1:
            house.append((i, j))
        elif cityMap[i][j] == 2:
            chicken.append((i, j))

for ch in combinations(chicken, m):
    dist = 0
    for h in house:   
        chickenDis = abs(ch[0][0] - h[0]) + abs(ch[0][1] - h[1]) 
        for j in range(1, m):  
            chickenDis = min(chickenDis, abs(ch[j][0] - h[0]) + abs(ch[j][1] - h[1]))  
        dist += chickenDis

    if(answer < 0):
        answer = dist
    else:
        answer = min(answer, dist)

print(answer)  


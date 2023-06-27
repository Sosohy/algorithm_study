n = int(input())
h = list(map(int, input().split()))
line = [0]*n

for i in range(n):
    tall = 0;
    
    for j in range(n):
        if(h[i] == tall) and (line[j] == 0):
            line[j] = i+1
            break

        if(line[j] == 0):
            tall += 1

ans = ' '.join(map(str, line))
print(ans)




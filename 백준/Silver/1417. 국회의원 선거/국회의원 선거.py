n = int(input())
result = [0]*n;

for i in range(n):
    result[i] = int(input())

cnt = 0   
if(n > 1): 
    tmp = result[1:]
    while((result[0] + cnt) <= max(tmp)):
        cnt += 1
        tmp[tmp.index(max(tmp))] -= 1;

print(cnt)
    
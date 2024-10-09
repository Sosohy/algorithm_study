N = int(input())

answer = 0

v1 = [0]*N # 같은 칸(j) 없는지
v2 = [0]*(2*N) # 대각선
v3 = [0]*(2*N) # 대각선

def queen(i):
    global answer
    if(i == N):
        answer += 1
        return
    else:
        for j in range(N):
            if(v1[j] == v2[i+j] == v3[i-j] == 0):
                v1[j], v2[i+j], v3[i-j] = 1, 1, 1
                queen(i+1)
                v1[j], v2[i+j], v3[i-j] = 0, 0, 0

queen(0)

print(answer)

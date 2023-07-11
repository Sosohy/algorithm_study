t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    pr = list(map(int, input().split())) 
    idx = [i for i in range(0, n)]
    count = 0

    while(True):
        if pr[0] == max(pr):
            count += 1

            if(idx[0] == m):
                print(count)
                break
            else:
                pr.pop(0)
                idx.pop(0)
        else:
            pr.append(pr.pop(0))
            idx.append(idx.pop(0))
            
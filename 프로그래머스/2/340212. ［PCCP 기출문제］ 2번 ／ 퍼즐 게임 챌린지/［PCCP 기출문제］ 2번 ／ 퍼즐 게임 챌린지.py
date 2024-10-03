def solution(diffs, times, limit):
    answer = 0

    def checkLevel(d, t, l, m):
        time = 0
        for i in range(len(d)):
            if(d[i] <= m):
                time += t[i]
            else:
                time += (d[i]-m)*(t[i] + t[i-1]) + t[i]
            if(l < time):
                return False
        return True

    s, e = 1, max(diffs)
    mid = 0

    while(s <= e):
        mid = (s+e)//2

        if(checkLevel(diffs, times, limit, mid)):
            e = mid-1
        else:
            s = mid+1

    if checkLevel(diffs, times, limit, mid): return mid
    if checkLevel(diffs, times, limit, mid+1): return mid+1
    return mid-1
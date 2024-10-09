l, c = map(int, input().split())
cList = sorted(list(map(str, input().split())))

used = ['']*l

def pw(idx):
    if(idx == l):
        con, vo = 0, 0
        for i in used:
            if(i in "aeiou"):
                vo += 1
            else:
                con += 1
        if(vo >= 1 and con >= 2):
            print("".join(used))
    else:
        s = 0 if idx == 0 else cList.index(used[idx-1])+1

        for i in range(s, c):
            used[idx] = cList[i]
            pw(idx+1)
            used[idx] = ''

pw(0)

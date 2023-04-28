s = input()
splitStr = s.split('-')

ans = 0

for i in splitStr[0].split('+'):
    ans += int(i)

splitStr.pop(0)

for i in splitStr:
    
    tmp  = i.split('+')
    for j in tmp:
        ans -= int(j)

print(ans)
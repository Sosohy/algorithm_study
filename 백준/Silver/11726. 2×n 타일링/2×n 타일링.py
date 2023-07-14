n = int(input())

addList = [0]

if(n<3):
    print(n)
else:
    for i in range(1, n+1):
        if(i<=2):
            addList.append(i)
        else:
            addList.append(addList[i-2]+addList[i-1])
    
    print(addList[n]%10007)


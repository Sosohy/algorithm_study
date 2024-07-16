n = int(input())
meet = set(["ChongChong"])

for i in range(n):
    n1, n2 = map(str, input().split())

    if(n2 in meet):
        meet.add(n1)
    elif(n1 in meet):
        meet.add(n2)
        
print(len(meet))
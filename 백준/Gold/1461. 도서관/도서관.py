n, m = map(int, input().split())
bookList = list(map(int, input().split()))
bookPlus = []
bookMinus = []
maxStep = 0

for i in bookList:
    if(maxStep < abs(i)):
        maxStep = abs(i)
        
    if(i > 0):
        bookPlus.append(abs(i))
    else:
        bookMinus.append(abs(i))
        
bookPlus.sort(reverse=True)
bookMinus.sort(reverse=True)


book = m
step = 0


for i in range(len(bookMinus)): #음수
    if(book == m):
        step += bookMinus[i]
    else:
        step += (bookMinus[i-1] - bookMinus[i])

    book -= 1    
    if(book == 0) or (i == len(bookMinus)-1):
        step += bookMinus[i]
        book = m

for i in range(len(bookPlus)): #양수
    if(book == m):
        step += bookPlus[i]
    else:
        step += (bookPlus[i-1] - bookPlus[i])

    book -= 1    
    if(book == 0) or (i == len(bookPlus)-1):
        step += bookPlus[i]
        book = m

print(step - maxStep)
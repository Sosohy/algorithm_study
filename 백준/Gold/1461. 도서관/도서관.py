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
#print(bookPlus, bookMinus)


book = m
step = 0


for i in range(len(bookMinus)):
    s = 0
    if(book == m):
        s = bookMinus[i]
    else:
        s = (bookMinus[i-1] - bookMinus[i])

    step += s
    #print(s, step)
    
    book -= 1    
    if(book == 0) or (i == len(bookMinus)-1):
        step += bookMinus[i]
        #print(bookMinus[i], step)
        book = m

for i in range(len(bookPlus)):
    s = 0
    if(book == m):
        s = bookPlus[i]
    else:
        s = (bookPlus[i-1] - bookPlus[i])

    step += s
    #print(s, step)
    
    book -= 1    
    if(book == 0) or (i == len(bookPlus)-1):
        step += bookPlus[i]
        #print(bookPlus[i], step)
        book = m

print(step - maxStep)
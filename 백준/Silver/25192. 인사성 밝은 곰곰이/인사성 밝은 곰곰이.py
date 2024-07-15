n = int(input())
answer = 0
emoticon = set()

for i in range(n):
    nickname = input()
    if(nickname == "ENTER"):
        answer += len(emoticon)
        emoticon = set()
    else:
        emoticon.add(nickname)

answer += len(emoticon)
print(answer)

def solution(genres, plays):
    answer = []
    musicDic = {}
    genresDic = {}
    
    for i in range(len(genres)):
        if genres[i] not in genresDic:
            genresDic[genres[i]] = plays[i]
            musicDic[genres[i]] = [(i, plays[i])]
        else:
            genresDic[genres[i]] += plays[i]
            musicDic[genres[i]].append((i, plays[i]))
            
    genreList = sorted(genresDic, key=lambda x:genresDic[x], reverse = True)
    
    for i in genreList:
        musicList = sorted(musicDic[i], key = lambda x: -x[1])
        #print(musicList)
        
        for j in musicList[:2]:
            answer.append(j[0])
        
    return answer
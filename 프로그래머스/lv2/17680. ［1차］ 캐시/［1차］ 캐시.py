from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        return len(cities)*5
    
    for i in cities:
        city = i.upper()
        if(len(cache) < cacheSize):
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                cache.append(city)
                answer += 5
        else:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                if(cache):
                    cache.popleft()
                cache.append(city)
                answer += 5
        
    return answer
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque() 
    #deque(maxlen=cacheSize) 이걸로 쓰면 (len(cache) >= cacheSize) 이 부분 안해줘도 됨!
    
    if cacheSize == 0:
        return len(cities)*5
    
    for i in cities:
        city = i.upper()
        
        if city in cache: # cache hit
                cache.remove(city)
                cache.append(city)
                answer += 1
        else: # cache miss
            if(len(cache) >= cacheSize): #캐시 크기보다 큰 경우 -> 제일 오래된 도시 pop
                if(cache):
                    cache.popleft()
            cache.append(city)
            answer += 5

    return answer
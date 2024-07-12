def solution(want, number, discount):
    answer = 0
    products = {want[i] : number[i] for i in range(len(want))}
    
    for i in range(10):  # 초기 10일 세팅
        p = discount[i]
        if(p in products):
            products[p] -= 1
    
    def checkProducts(products, want):
        for i in range(len(want)):
            if(products[want[i]] > 0):
                return False
        return True
        
    for i in range(10, len(discount)):
        
        # 상품 개수 체크
        if(checkProducts(products, want)):
            answer += 1
        
        # 지난 첫째날 상품 빼기(10일 이전 날짜) 
        if(discount[i-10] in products):
            products[discount[i-10]] += 1
        
        # 추가된 마지막날 상품 추가하기
        if(discount[i] in products):
            products[discount[i]] -= 1
            
    if(checkProducts(products, want)):
            answer += 1

    return answer
def solution(want, number, discount):
    answer = 0
    products = {want[i] : number[i] for i in range(len(want))}
    
    for i in range(10):  # 초기 10일 세팅
        if(discount[i] in products):
            products[discount[i]] -= 1
    
    # 모든 원하는 제품이 원하는 수량만큼 있는지 확인
    def checkProducts(products, want):
        return all(products[p] <= 0 for p in want)
    
    if(checkProducts(products, want)):
            answer += 1
        
    for i in range(10, len(discount)):

        # 지난 첫째날 상품 빼기(10일 이전 날짜) 
        if(discount[i-10] in products):
            products[discount[i-10]] += 1
        
        # 추가된 마지막날 상품 추가하기
        if(discount[i] in products):
            products[discount[i]] -= 1
            
        if(checkProducts(products, want)):
            answer += 1

    return answer
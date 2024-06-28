def solution(data, ext, val_ext, sort_by):
    answer = []
    order = ["code", "date", "maximum", "remain"]
    
    for i in data:
        extIdx = order.index(ext)
        if(i[extIdx] < val_ext):
            answer.append(i)
    
    answer = sorted(answer, key = lambda x : ( x[order.index(sort_by)]) )
    
    return answer
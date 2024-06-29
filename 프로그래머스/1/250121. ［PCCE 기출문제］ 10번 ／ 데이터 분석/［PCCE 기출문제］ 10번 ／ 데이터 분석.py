def solution(data, ext, val_ext, sort_by):
    answer = []
    order = ["code", "date", "maximum", "remain"]
    
    extIdx = order.index(ext)
    for i in data:
        if(i[extIdx] < val_ext):
            answer.append(i)
    
    answer = sorted(answer, key = lambda x : ( x[order.index(sort_by)]) )
    
    return answer
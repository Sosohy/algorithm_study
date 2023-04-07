def solution(board, moves):
    answer = 0
    basket = [0]
    
    for i in moves:
        for x in board:
            if(x[i-1]) != 0:
                doll = x[i-1]
                if basket[-1] != doll:
                    basket.append(doll)
                else:
                    basket.pop()
                    answer += 2
                x[i-1] = 0
                break;
    
    return answer
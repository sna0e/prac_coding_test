# P87389 - 나머지가 1이 되는 수 찾기

def solution(n):
    answer = n
    
    for i in range (n, 0, -1) :
        if (n % i == 1) & (i < answer) :
            answer = i
    
    return answer
    
    
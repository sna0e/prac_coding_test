# P12931 - 자릿수 더하기

def solution(n):
    answer = 0

    for i in range (len(str(n))) :
        answer += int(str(n)[i])
    
    
    return answer
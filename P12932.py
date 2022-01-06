# P12932 - 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    
    l = list(reversed(str(n)))
    
    for i in range (len(l)) :
        answer.append(int(l[i]))
        
    return answer
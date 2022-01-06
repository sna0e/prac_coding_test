# P12906 - 같은 숫자는 싫어

def solution(arr):
    
    answer = []
    
    
    for i in range (len(arr)) :
        if len(answer) == 0 :
            answer.append(arr[i])
        elif answer[-1] != arr[i] :
            answer.append(arr[i])
    
    return answer


# 효율성 테스트 실패한 거 ↓
# 이유는 ? =>

def solution(arr):
    
    i = 1
    while i < len(arr) :
        if arr[i-1] == arr[i] :
            arr.pop(i)
        else :
            i += 1
            
    return arr
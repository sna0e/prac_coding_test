# P12928 - 약수의 합

def solution(n):
    answer = 0
    
    i = 1
    while n // i >= i :
        if n / i == i :
            answer += i
        elif n % i == 0 :
            answer = answer + i + n // i
        i += 1
    return answer
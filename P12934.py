# P12934 - 정수 제곱근 판별

# 모듈 사용
import math

def solution(n):
    if (math.isqrt(n)**2 == n) :
        return ((math.sqrt(n)+1)**2)
    else :
        return -1
    
# 모듈 사용 x
def solution(n) :
    if (int(n**(1/2))**2 == n) :
        return ((n**(1/2)+1)**2)
    else :
         return -1
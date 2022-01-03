# P12935 - 제일 작은 수 제거하기

def solution(arr):
    if len(arr) == 1 :
        return [-1]
    least = min(arr)
    
    while True :
        try :
                arr.remove(least)
        except (ValueError) :
            return arr
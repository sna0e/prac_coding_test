# P12917 - 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''
    s = sorted(s, reverse=True)
    for i in range (len(s)) :
        answer += s[i]
    return answer
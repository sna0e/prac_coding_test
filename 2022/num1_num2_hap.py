def solusion(a, b):
    answer = 0
    x = a
    if(a <= b) :
        for x in range (a,b+1,1) :
            answer += x
    else :
        for x in range (b, a+1, 1):
            answer += x
    
    return answer

print(solusion(5,3))

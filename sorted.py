def solutinos(s) :
    
    answer = ""
    char = sorted(s, reverse = True)
    for i in range(len(char)) :
        answer += char[i]

    return answer

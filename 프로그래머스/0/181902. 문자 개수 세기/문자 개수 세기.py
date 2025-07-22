def solution(my_string):
    alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    for i in range(ord('a'),ord('z')+1):
        alphabet.append(chr(i))
    answer = [0]*52
    for i in range(len(my_string)):
        for j in range(len(alphabet)):
            if my_string[i] == alphabet[j]:
                answer[j]+=1
                
    
    return answer
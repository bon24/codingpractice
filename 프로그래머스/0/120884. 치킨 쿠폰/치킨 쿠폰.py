def solution(chicken):
    service = 0 
    while chicken >= 10:
        service += chicken // 10
        chicken = (chicken//10)+(chicken % 10)
    return service
    # answer = 0
    # ticket=0
    # while chicken >= 10:
    #     ticket += chicken%10
    #     chicken = chicken//10
    #     ticket+=1
    #     answer+=chicken
    # ticket+=chicken
    # if ticket > 10 :
    #     answer+=ticket//10
    # return (chicken-1)//9
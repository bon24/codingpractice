def solution(polynomial):
    sum_x = 0
    sum_int = 0
    if len(polynomial)==1:
        return polynomial
    for term in polynomial.split(" + "): 
        if "x" in term:                  
            num = term.replace("x", "")
            sum_x += int(num) if num else 1
        else:                             
            sum_int += int(term)

    if sum_x and sum_int:
        if sum_x==1:
            sum_x=''
        return f"{sum_x}x + {sum_int}"
    elif sum_x:
        return f"{sum_x}x"
    else:
        return str(sum_int)
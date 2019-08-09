def calc_add(num1,num2):
    return(num1+num2)

def calc_sub(num1,num2):
    if num1>num2:
        return num1-num2
    else:
        return num2-num1

def calc_mul(num1,num2):
    return num1*num2

def calc_div(num1,num2):
    if num2==0:
        print("divide by zero exception\n")
    else:
        return(num1/num2)

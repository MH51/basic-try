def fun(n1,n2,n3):
    if n1>n2 and n1>n3:
        return(n1 ,"is largest")
    elif n2>n3:
        return(n2,"largest")
    else:
        return(n3,"largest")
n1=int(input('enter num1: '))   
n2=int(input('enter num2: ')) 
n3=int(input('enter num3: '))      
print(fun(n1,n2,n3))

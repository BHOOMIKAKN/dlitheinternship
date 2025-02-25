#fib
def tib(n):
    
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return tib(n-1)+tib(n-2)+tib(n-3)


n=int(input("enter the number to find tribnocii: "))
for i in range(n):
    #c=fib(n)
    print(tib(i))
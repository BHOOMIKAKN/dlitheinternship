#fib
def fib(n):
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


n=int(input("enter the number to find fibnocii: "))
for i in range(n):
    #c=fib(n)
    print(fib(i))
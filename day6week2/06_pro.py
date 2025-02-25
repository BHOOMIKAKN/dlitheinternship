#sum of number
def pro(n):
    prod=1
    while n>0:
        prod=prod*(n%10)
        n//=10
    print(prod)


num=int(input("Enter the number to get product: "))
pro(num)
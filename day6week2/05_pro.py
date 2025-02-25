#sum of number
def sum(n):
    sum=0
    while n>0:
        sum=sum+(n%10)
        n//=10
    print(sum)


num=int(input("Enter the number to get sum: "))
sum(num)
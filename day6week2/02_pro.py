#binary to decimal
def bin2dec(n):
    sum=0
    while n>0:
        for i in range(n):
            sum=sum+((n%10)*2**i)
            n//=10
        print(sum)



bin=int(input("Enter the binary number to convert into decimal: "))
bin2dec(bin)
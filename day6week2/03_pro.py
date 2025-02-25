#decimal to binary
def dec2bin(n):
    sum=" "
    while n>0:
        rem=n%2
        n//=2
        sum=str(rem)+sum
        
    print(sum)



dec=int(input("Enter the decimal number to convert into binary: "))
dec2bin(dec)
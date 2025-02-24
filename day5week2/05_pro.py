a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
c=int(input("Enter number3: "))
if a>b and a>c:
    print(f"{a} is largest")
elif b>a and b>c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")
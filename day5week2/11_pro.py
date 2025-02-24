def mul(n):
    for i in range(1,11):
        b=i*n
        print(f"{n}*{i}={b}")

n=int(input("Enter the table user required: "))
mul(n)
def fullpat(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()

def halfpat(n):
    for i in range(n+1):
    
            print(" " * (n-i),end=" ")
            print("* " * i)
        


pattern=int(input("Enter the number for which patters required: "))
fullpat(pattern)
halfpat(pattern)

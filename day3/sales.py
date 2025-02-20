comp1=int(input("Enter the sales of company 1: "))
comp2=int(input("Enter the sales of company 2: "))
comp3=int(input("Enter the sales of company 3: "))
if comp1==comp2==comp3:
    print("All have same number of sales")
elif comp1>comp2 and comp1>comp3:
    print("Company 1 sales is more")
elif comp2>comp1 and comp2>comp3:
    print("Comapny 2 sales is more")
else:
    print("Company 3 sales is more")
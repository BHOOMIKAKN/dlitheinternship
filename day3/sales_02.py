month1=int(input("Enter the first month sales: "))
month2=int(input("Enter the second month sales: "))
month3=int(input("Enter the third month sales: "))
total_sales=month1+month2+month3
if total_sales>=90000:
    print("Person can continue!!")
elif total_sales>=70000:
    print("Person is in medium range and can continue")
else:
    print("Person is not eligible to continue his/her job")
#palindrome
a=str(input("Enter the value to check for palindrome: "))
rev=a[::-1]
#print(rev)
if a==rev:
    print(f"{a} is palindrome ")
else:
    print(f"{a} is not a palindrome")

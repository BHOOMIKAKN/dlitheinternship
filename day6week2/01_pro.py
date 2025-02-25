#list is sorted or not check

lists=list(input("ENter the list: "))
#print(lists)
rev=lists
#print(rev)
rev.sort()
#print(rev)
if rev==lists:
    print("True")
else:
    print("False")
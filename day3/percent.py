max=int(input("Enter the maximum marks: "))
score=int(input("Enter the obtained marks: "))
marks=(score/max)*100
print("Percentage of Student is ",marks)
if marks>=90:
    print("Grade is A")
elif marks>=80:
    print("Grade is B")
elif marks>=70:
    print("Grade is C")
elif marks>=60:
    print("Grade is D")
elif marks>=50:
    print("Grade is E")
else:
    print("Grade is F")
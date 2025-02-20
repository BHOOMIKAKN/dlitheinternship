score=int(input("Enter the score of the Student: "))
if score>=80:
    print("The Student is Pass!!!")
elif score<80 and score>=75:
    print("The student is failed but can apply for re-examination")
else:
    print("Student is failed")
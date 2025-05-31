name = str(input("Enter your name : "))
age = int(input("Enter your age : "))
gpa = float(input("Enter your gpa(0-5) : "))
interestedField = str(input("Enter your interested field : "))
graduated = input("Are you graduated : ")

if graduated == "Yes":
    print("I am graduated")
else:
    print("I am not graduated")

if(age<25 and gpa>=3.5 and graduated=="Yes"):
    print("the user is eligible for a scholarship")
elif(age < 30 and gpa >= 2.5):
    print("he user is eligible for an internship")
else:
    print("recommend they apply again later")
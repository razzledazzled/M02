##  Name: Anthony Harris
##  File Name: M02_Lab_DeansList.py
##  This program asks XXX

lastNameInputText = ("Please enter the last name of student {}: ")
firstNameInputText = ("Please enter the first name of student {}: ")
counter = 1
studentList = []
gpaList = []

print("Student GPA Tracker")
print()
lastName = (input(lastNameInputText.format(counter)))

while lastName != "ZZZ":
    firstName = (input(firstNameInputText.format(counter)))
    fullName = (firstName.strip()).capitalize() + " " + (lastName.strip()).capitalize()
    
    gpa = int((input("What is {}'s GPA?: ".format(fullName))))

    lastName = (input(lastNameInputText.format(counter + 1)))

print("End Program")
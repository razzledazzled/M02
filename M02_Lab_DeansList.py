##  Name: Anthony Harris
##  File Name: M02_Lab_DeansList.py
##  This program asks XXX

##  Variables
lastNameInputText = ("Please enter the last name of student {} or type \"ZZZ\" to quit: ")
firstNameInputText = ("Please enter the first name of student {}: ")
counter = 1  #Counts +1 for each student
studentList = [] #List of all students
gpaList = [] #List of all gpas

#Start of main program
print("Student GPA Tracker")
print()
#Asks user for student last name 
lastName = (input(lastNameInputText.format(counter)))

while lastName != "ZZZ":
    #Inializes repeate variables
    isGpaFlag = False

    #Asks user for student first name
    firstName = (input(firstNameInputText.format(counter)))

    #Removes white space from both strings, captalizes the first letter of both strings, 
    #concatenates both strings with one space between the strings -> written to fullName
    fullName = (firstName.strip()).capitalize() + " " + (lastName.strip()).capitalize()
    
    #Adds fullName to a list
    studentList.append(fullName)

    #Asks user for student's gpa
    while True:
        sGpa = input("What is {}'s GPA?: ".format(fullName))

        try:
            fGpa = float(sGpa)  # Convert input GPA to float
            break  # Exit the inner loop if a valid GPA is entered
        except ValueError:
            print("Invalid GPA entered. Please enter a valid numeric value.")
            continue  # Skip the rest of the loop and start from the beginning

    #Adds gpa to list
    gpaList.append(fGpa)

    #Ask user for last name again, checking for "quit" value
    lastName = (input(lastNameInputText.format(counter + 1)))

#Prints both lists
print(studentList)
print(gpaList)
print("End Program")
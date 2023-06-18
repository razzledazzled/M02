##  Name: Anthony Harris
##  File Name: M02_Lab_DeansList.py
##  This program asks the user for a student's last name.
##  If the name is ZZZ, then the program prints all recorded and quits.
##  Progam will ask for last name, then first, then combines both names.
##  The program will elimnate white space and capitalize names
##  The program then asks for a gpa, if gpa is not on 4.0 scale (0.0-4.0)
##  then the program will loop until the user enters the correct data.
##  The program then checks to see if the a valid gpa is eligable for 
##  Dean's List (3.5) or Honor Roll (3.25).
##  Program loops until ZZZ is entered.

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
            if (fGpa > 4.0 or fGpa < 0.0): #If gpa not on scale, repeate loop
                print("Invalid GPA entered. Please enter a GPA within the 4.0 scale.")
            else:
                break  # Exit the inner loop if a valid GPA is entered
        except ValueError:
            print("Invalid GPA entered. Please enter a valid numeric value.")
            continue  # Skip the rest of the loop and start from the beginning

    #Adds gpa to list
    gpaList.append(fGpa)

    if fGpa >= 3.5: #If gpa is greater than or equal to 3.5
        print("Congrats! {} made the Dean's List with a {} GPA!".format(fullName, sGpa))
    elif fGpa >= 3.25: #If gpa is greater than or equal to 3.25
        print("Awesome! {} made the Honor Roll with a GPA of {}!".format(fullName,sGpa))

    #Ask user for last name again, checking for "quit" value
    lastName = (input(lastNameInputText.format(counter + 1)))

#Prints both lists
print(studentList)
print(gpaList)
print("End Program")
############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Dan Shaw w0190983

# I'm using global variables for constants only. Everything else will remain local as per your request
CLASSES = [ "PROG1700", "NETW1024", "OSYS1200", "WEBD1000", "DBAS1001", "COMM1700" ]
VALID_GRADES = ["A", "B", "C", "D", "F"] # I've disincluded E from this list because the instructions printed to the user only ask for ABCDF
VALID_MODS = ["+", "-", ""]

# main() FUNCTION
def main():

    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

    numericGrade = 0.0
    grades = []

    for i in range(len(CLASSES)):
        #Gather user inputs
        results = getGrade(CLASSES[i])
        numericGrade = calculateNumeric(results[0], results[1])
        grades.append(numericGrade)
    
    print("*" * 50)
    for i in range(len(CLASSES)):
        # Output final message and result, with formatting
        print("The numeric value for {1} is: {0:.1f}".format(grades[i], CLASSES[i]))

    print("Your grade point average for the semester is: {0:.1f}".format(calculateAverage(grades)))

def calculateAverage(grades:list):
    return (sum(grades) / len(grades))

def calculateNumeric(letterGrade, modifier):
    # Determine base numeric value of the grade
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        #If an invalid entry is made
        print("You entered an invalid letter grade.")

    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3

    return numericGrade

def getGrade(course):
    # Some input validation to make sure the user entered valid values for both letterGrade and modifier
    while (letterGrade := input("Please enter a letter grade for {0}\n> ".format(course)).upper()) not in VALID_GRADES:
        print("Invalid Input. Must be between A and F".format(course))

    while (modifier := input("Please enter a modifier (+, -, or nothing)\n> ")) not in VALID_MODS:
        print("Invalid modifier. Please enter only +, -, or leave blank")

    return letterGrade, modifier

#PROGRAM EXECUTION STARTS HERE
if __name__ == "__main__":
    main()
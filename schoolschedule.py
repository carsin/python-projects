fname = input("What is your first name?")
lname = input("What is your last name?")

studentId = int(input("Student ID: "))

currClass = "init"

classes = []
classNums = []

while (currClass.lower() != "stop"):
    currClass = input("Enter the next class, STOP to end.\t")
    if (currClass.lower() != "stop"):
        classNum = int(input("Enter the room number: "))
        classes.append(currClass)
        classNums.append(classNum)
    else:
        print("*********************************************")
        print("*\t\t\t\t\t*")
        print("* " + lname + ", " + fname + "\t \t ID: " + str(studentId) + " \t*")
        print("*********************************************")
        print("*\t\t\t\t\t*")

        for x in range (0, len(classes)):
            print("* Block " + str(x + 1) + ": " + classes[x] + "\t Room: " + str(classNums[x]) + "\t *")

        print("*********************************************")

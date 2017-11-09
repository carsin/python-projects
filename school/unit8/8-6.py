# Its so messy :/
def GPAcalc(letter, weighted):
    if (weighted == 0):
        weighted = False
    elif (weighted == 1):
        weighted = True
    else:
        print("Invalid weight value.")

    letter = letter.lower()
    if (letter == "a"):
        if (weighted):
            return 5
        else: 
            return 4
    elif (letter == "b"):
        if (weighted):
            return 4   
        else: 
            return 3
    elif (letter == "c"):
        if (weighted):
            return 3
        else: 
            return 2
    elif (letter == "d"):
        if (weighted):
            return 2
        else: 
            return 1
    elif (letter == "f"):
        if (weighted):
            return 1  
        else: 
            return 0
    else:
        return "Invalid"

grades = []
    
def getClassGrades():
    classNum = int(input("How many classes are you taking? "))
    for i in range(0, classNum):
        grade = input("Enter your Letter Grade: ")
        weighted = int(input("Is it weighted?(1 = yes, 0 = no) "))
        grades.append(GPAcalc(grade, weighted))
    
    print("Your weighted GPA is a " + str(sum(grades) / len(grades)))

float(123.2)
    
getClassGrades()

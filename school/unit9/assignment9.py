'''
In this program you will create a personal organizer. Using parallel arrays you will store the following information on each event in your organizer:

Month (1 - 12)
Day (1 - 31)
Year
Event name

If the user enters an incorrect month the month should be set to January.
If the user enters an incorrect day then the day should be set to 1.


Write the following methods:

Add an event
Print all events
Print events in a specific month
'''
eventMonths = []
eventDays = []
eventYears = []
eventNames = []

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def addEvent(month, day, year, name):
    eventMonths.append(month)
    eventDays.append(day)
    eventYears.append(year)
    eventNames.append(name)
    
def printAllEvents():
    print("******************** List of Events ********************")
    for i in range(len(eventMonths)):
        print(str(eventNames[i]))
        print("Date: " + str(months[eventMonths[i] - 1]) + " " + str(eventDays[i]) + ", " + str(eventYears[i]))
        
def printEventsInMonth(monthNum):
    print("********** Events in " + months[monthNum - 1] + "**********")
    for i in range(len(eventMonths)):
        if (eventMonths[i] == monthNum):
            print(str(eventNames[i]))
            print("Date: " + str(months[eventMonths[i] - 1]) + " " + str(eventDays[i]) + ", " + str(eventYears[i]))

def start():
    enterAnotherDate = None
    while (enterAnotherDate != "NO"):
        eventName = input("What is the event: ")
        eventMonth = int(input("What is the month (number): "))
        if (eventMonth > 12 or eventMonth < 1):
            eventMonth = 1
        eventDay = int(input("What is the date: "))
        if (eventDay > 31 or eventDay < 1):
            eventDay = 1
        eventYear = int(input("What is the year: "))
        addEvent(eventMonth, eventDay, eventYear, eventName)
        enterAnotherDate = input("Do you want to enter another date? NO to stop.")
    
    printAllEvents()
    monthToSee = int(input("What month would you like to see? (Enter the month number)"))
    printEventsInMonth(monthToSee)
    
start()

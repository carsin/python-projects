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
    for i in range(eventMonths.len)
        print(str(eventNames[i]))
        print(str("Date: " + months[eventMonths[i] - 1] + eventDays[i] + ", " + eventYears[i]))

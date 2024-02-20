def add_time(start, duration, *day):
    startSplit = start.split()
    startFormat = startSplit[1]
    startSepartorPos = 0
    durationSepartorPos = 0

    # Getting the index of the ':'
    for i in range(len(startSplit[0])):
        if startSplit[0][i] == ":":
            startSepartorPos = i
    for i in range(len(duration)):
        if duration[i] == ":":
            durationSepartorPos = i

    # Gettings time as int values.
    startHours = int(startSplit[0][:startSepartorPos])
    startMinutes = int(startSplit[0][startSepartorPos + 1 :])
    durationHours = int(duration[:durationSepartorPos])
    durationMinutes = int(duration[durationSepartorPos + 1 :])

    # Removing the time format AM/PM into a 24H format.
    if startFormat == "PM":
        startHours += 12

    # Adding the minutes and keeping hours to add if needed.
    newMinutes = startMinutes + durationMinutes
    addHours = 0
    if newMinutes / 60 > 1:
        addHours = int(newMinutes / 60)
        newMinutes = newMinutes - 60

    # Adding the hours and keeping day to add if needed.
    newHours = startHours + durationHours + addHours
    addDay = 0
    if newHours / 24 > 1:
        addDay = int(newHours / 24)
        newHours = newHours - 24 * addDay

    # Transforming 24h to 12AM
    if newHours == 24:
        newHours = 12
    # Check if PM or AM
    amFormat = "AM"
    if newHours == 12 and startSplit[1] == "AM":
        amFormat = "PM"
    elif newHours == 12 and startSplit[1] == "PM":
        amFormat = "AM"
    elif newHours == 0:
        newHours = 12
        amFormat = "AM"
    elif newHours > 12:
        amFormat = "PM"
    if newHours > 12:
        newHours -= 12

    # Check if minutes is < 10 to add a zero
    newMinutesStr = ""
    if newMinutes < 10:
        newMinutesStr = "0" + str(newMinutes)
    else:
        newMinutesStr = str(newMinutes)

    # Check if a day as passed.
    dayPassed = ""
    if addDay > 0:
        if addDay > 1:
            dayPassed = "(" + str(addDay) + " days later)"
        else:
            dayPassed = "(next day)"

    # Keeping count of day.
    dayName = None
    try:
        # Get start Day Nb
        day = day[0].lower()
        startDayNb = 0
        match day:
            case "monday":
                startDayNb = 0
            case "tuesday":
                startDayNb = 1
            case "wednesday":
                startDayNb = 2
            case "thurday":
                startDayNb = 3
            case "friday":
                startDayNb = 4
            case "saturday":
                startDayNb = 5
            case "sunday":
                startDayNb = 6

        # Get End Day nB
        endDay = addDay + startDayNb
        while endDay >= 7:
            endDay = endDay - 7
        match endDay:
            case 0:
                dayName = "Monday"
            case 1:
                dayName = "Tuesday"
            case 2:
                dayName = "Wesnesday"
            case 3:
                dayName = "Thurday"
            case 4:
                dayName = "Friday"
            case 5:
                dayName = "Saturday"
            case 6:
                dayName = "Sunday"
    except:
        pass

    # Formating ouput:
    if addDay > 0 and dayName is None:
        new_time = (
            str(newHours) + ":" + newMinutesStr + " " + amFormat + " " + dayPassed
        )
    elif addDay > 0 and dayName is not None:
        new_time = (
            str(newHours)
            + ":"
            + newMinutesStr
            + " "
            + amFormat
            + ", "
            + dayName
            + " "
            + dayPassed
        )
    elif dayName is not None:
        new_time = str(newHours) + ":" + newMinutesStr + " " + amFormat + ", " + dayName
    else:
        new_time = str(newHours) + ":" + newMinutesStr + " " + amFormat
    return new_time

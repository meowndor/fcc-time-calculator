def minuteconverter(time):

    if time[-2:] == "PM":
        thehour = int(time[0: time.index(":")])
        theminute = int(time[time.index(":") + 1: time.index(" ")])
        minutes = (12 + thehour)*60 + theminute

    elif time[-2:] == "AM":
        thehour = int(time[0: time.index(":")])
        theminute = int(time[time.index(":") + 1: time.index(" ")])
        minutes = thehour*60 + theminute
    else:
        thehour = int(time[0: time.index(":")])
        theminute = int(time[time.index(":") + 1:])
        minutes = thehour*60 + theminute
    return int(minutes)


def add_time(start, duration, startingday=None):
    daysofweek = ["Monday", "Tuesday", "Wednesday",
                  "Thursday", "Friday", "Saturday", "Sunday"]

    totalminutes = minuteconverter(start) + minuteconverter(duration)  # 2881
    minutesremainder = totalminutes % 60  # 1

    totalhours = (totalminutes - minutesremainder)/60  # (2881-1)/60=48
    hoursremainder = totalhours % 24  # 0

    totaldays = int((totalhours - hoursremainder) / 24)  # (48-0)/24 = 2

    theday = ""
    suffix = ""
    # suffix for AM PM
    if hoursremainder == 24:
        hoursremainder = 0

    if hoursremainder >= 0 and hoursremainder < 12:
        suffix = "AM"
    elif hoursremainder >= 12 and hoursremainder <= 23:
        suffix = "PM"

    # theday
    # if starting day is not empty
    if startingday != None:
        if totaldays == 1:
            theday = f", {(daysofweek[(daysofweek.index(startingday.capitalize())+totaldays)%len(daysofweek)])} (next day)"
        if totaldays == 0:
            theday = f", {startingday}"
        elif totaldays > 1 and startingday != None:
            theday = f", {(daysofweek[(daysofweek.index(startingday.capitalize())+totaldays)%len(daysofweek)])} ({totaldays} days later)"
    # if starting day is empty
    elif startingday == None:
        if totaldays == 1:
            theday = " (next day)"
        elif totaldays > 1:
            theday = f" ({totaldays} days later)"

    # turns 12 AM instead of 0 AM
    if hoursremainder == 0:
        hoursremainder = 12

    if hoursremainder > 12:
        new_time = f"{hoursremainder-12:g}:{minutesremainder:02d} {suffix}{theday}"
    else:
        new_time = f"{hoursremainder:g}:{minutesremainder:02d} {suffix}{theday}"

    return new_time

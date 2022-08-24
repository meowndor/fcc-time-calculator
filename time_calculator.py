def minuteconverter(time):

    if time[-2:] == "PM":
        thehour = int(time[0: time.index(":")])
        theminute = int(time[time.index(":") + 1: time.index(" ")])
        minutes = (12 + thehour)*60 + theminute

    else:
        thehour = int(time[0: time.index(":")])
        theminute = int(time[time.index(":") + 1:])
        minutes = thehour*60 + theminute
    return int(minutes)


def add_time(start, duration):
    totalminutes = minuteconverter(start) + minuteconverter(duration)
    new_time2 = f"{(totalminutes - totalminutes % 60)/60:g}:{totalminutes%60:02d}"

    if int(new_time2[:new_time2.index(":")]) > 12:
        new_time = f"{int(new_time2[:new_time2.index(':')])-12:g}:{totalminutes%60:02d} PM"
    else:
        new_time = f"{new_time2:g} : {totalminutes%60:02d} AM"
    return new_time


# print(minuteconverter("2:01"))
print(add_time("3:00 PM", "2:01"))

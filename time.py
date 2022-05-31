def time():
    start = input("Start: ")
    startHour = 0
    startMin = 0
    if len(start) == 4:
         startHour = int(start[0:2])
         startMin = int(start[2:])
    else:
        startHour = int(start[0:1])
        startMin = int(start[1:])
    startMin /= 60
    startTime = startHour + startMin
    print()
    lunchStart = input("Break Start: ")
    lunchHour = 0
    lunchMin = 0
    if len(lunchStart) == 4:
         lunchHour = int(lunchStart[0:2])
         lunchMin = int(lunchStart[2:])
    else:
        lunchHour = int(lunchStart[0:1])
        lunchMin = int(lunchStart[1:])
    lunchMin /= 60
    lunchStart = lunchHour + lunchMin
    print()
    lunchEnd = input("Break End: ")
    lunchHour = 0
    lunchMin = 0
    if len(lunchEnd) == 4:
         lunchHour = int(lunchEnd[0:2])
         lunchMin = int(lunchEnd[2:])
    else:
        lunchHour = int(lunchEnd[0:1])
        lunchMin = int(lunchEnd[1:])
    lunchMin /= 60
    lunchEnd = lunchHour + lunchMin
    print()
    timeWorked = 12 - startTime + lunchStart
    hoursRemaining = 8 - timeWorked
    endTime = hoursRemaining + lunchEnd
    minutes = (endTime % 1) * 60
    hours = int(endTime)
    amOrPm = ' pm'
    if hours > 12:
        amOrPm = ' am'
        hours -= 12
    if len(str(int(minutes))) == 1:
        minutes = '0' + str(int(minutes))
    else:
        minutes = int(minutes)
    print("End work today at ", hours, ":", minutes, amOrPm)
time()

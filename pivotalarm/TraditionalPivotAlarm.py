import time


def traditionalPivotAlarm(srVar, dsVar, ltpC):
    # start_time = time.time()

    # alarm expiry in minutes
    alarmExp = 30

    ltpP = dsVar["C"]

    # Area width calculation (adt)
    width = 0.04
    pivot = srVar[7]
    adt = pivot * width / 100
    
    refT = dsVar['refT']
    alarmTimer = dsVar['alarmTimer']
    srType = dsVar["srT"]
    srValue = dsVar["srValue"]

    # condition for alarm timer and ltp data
    if alarmTimer > 0:
        alarmTimer = alarmExp * 60 - (time.time() - refT)

    # condition for no value
    elif ltpC == 0:
        refT = 0
        alarmTimer = 0
        srType = "None"
        srValue = 0

    # condition for checking pivot alarm
    else:
        refT = 0
        alarmTimer = 0
        srType = "None"
        srValue = 0
        for i in range(1, 14):
            # print(srVar[i])
            diffCOne = srVar[i] - ltpC
            diffPOne = srVar[i] - ltpP
            diffCTwo = srVar[i + 1] - ltpC
            diffPTwo = srVar[i + 1] - ltpP

            # outside condition
            if(diffCOne < 0 and diffPOne < 0) and (diffCTwo < 0 and diffPTwo < 0):
                continue

            # on surface condition for left side
            elif srVar[i] <= ltpC <= srVar[i] + adt:
                refT = time.time()
                alarmTimer = alarmExp * 60
                srValue = srVar[i]
                if ltpC > pivot:
                    srType = "R"
                else:
                    srType = "S"
                break

            # On surface condition for right side
            elif srVar[i + 1] - adt <= ltpC <= srVar[i + 1]:
                refT = time.time()
                alarmTimer = alarmExp * 60
                srValue = srVar[i+1]
                if ltpC > pivot:
                    srType = "R"
                else:
                    srType = "S"
                break

            # condition for no crossing
            elif (diffCOne < 0 and diffPOne < 0) and (diffCTwo > 0 and diffPTwo > 0):
                break

            # condition for left crossing
            elif (diffCOne < 0 and diffPOne < 0) and (diffCTwo > 0 > diffPTwo):
                refT = time.time()
                alarmTimer = alarmExp * 60
                srValue = srVar[i + 1]
                srType = "S"
                break

            # condition for right crossing
            elif (diffCOne < 0 < diffPOne) and (diffCTwo > 0 and diffPTwo > 0):
                refT = time.time()
                alarmTimer = alarmExp * 60
                srValue = srVar[i]
                srType = "R"
                break

            # on surface condition for left side for past
            elif srVar[i] <= ltpP <= srVar[i] + adt:
                refT = time.time()
                alarmTimer = alarmExp * 60
                srValue = srVar[i]
                if ltpC > pivot:
                    srType = "R"
                else:
                    srType = "S"
                break

            # On surface condition for right side for past
            elif srVar[i + 1] - adt <= ltpP <= srVar[i + 1]:
                refT = time.time()
                alarmTimer = alarmExp * 60
                srValue = srVar[i + 1]
                if ltpC > pivot:
                    srType = "R"
                else:
                    srType = "S"
                break

            # not define condition
            else:
                refT = 0
                alarmTimer = 0
                srType = "None"
                srValue = 0
                break

    return alarmTimer, refT, srType, srValue

time12 = input()
time24 = time12[2:-2]
AP = time12[-2:]
hour = int(time12[:2])
if AP == 'AM':
    if hour == 12:
        hour = '00'
    elif hour >= 10:
        hour = str(hour)
    else:
        hour = '0' + str(hour)
else:
    if hour == 12:
        hour = '12'
    else:
        hour = str(hour+12)
print(hour + time24)
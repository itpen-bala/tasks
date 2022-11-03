# create function, that accepts hour and minute and returns angle between hour hand and minute hand 

def calc_angle(hour: int, minute: int) -> int:
    if (hour < 0 or hour > 12) or not isinstance(hour, int):
        print("hour must be integer number between 0 and 12")
        return -1
    if (minute < 0 or minute > 60) or not isinstance(minute, int):
        print("minute must be integer number between 0 and 60")
        return -1
    if hour == 12:
        hour = 0
    if minute == 60:
        minute = 60
    
    minute_angle = 360 / 60 * minute
    int_hour_angle = 360 / 12 * hour
    fract_hour_angle = 360 / 12 / 60 * minute
    hour_angle = int_hour_angle + fract_hour_angle
    angle_between_hour_and_minute = abs(minute_angle - hour_angle)
    
    return int(angle_between_hour_and_minute)


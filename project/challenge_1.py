# converting 12 hour time to 24 hour time

# this function takes in one argument and that is time
def convert_time(s):
    # we are using destructuring method to access the value of time we want to convert
    
    # period is for accessing the last value that is either "PM " or "AM"
    period = s[-2:]
    # get hold on the whole time
    time = s[:-2]
    # used to get hold on the hour
    hour = int(time[:2])
    
    # this if statement is used to convert the value based on the the period and hour
    if period == 'PM' and hour < 12:                
        time = str(hour + 12) + time[2:]

    if period == 'AM' and hour == 12:
        time = '00' + time[2:] 
        
    return time

print(convert_time("10:30 PM"))
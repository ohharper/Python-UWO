def seconds_in_day ():
    hours_in_day = 24
    mins_in_hour = 60
    sec_in_min = 60
    return hours_in_day * mins_in_hour * sec_in_min 
 
# Call the function and display the number of seconds in a day from the return statement
print(seconds_in_day())
 
# or
print(f"There are {seconds_in_day()} seconds in a day!")
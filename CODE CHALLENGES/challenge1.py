def convert_to_24_hour(hour, minute, period):
    if period == "am":               # Checks if the period is in am
        if hour == 12:               # If it's 12 am, then converts that hour to 0
            hour = 0
    else:
        if hour != 12:               # If period is in pm & not 12 pm, it adds 12 to the hour
            hour += 12
    return f"{hour:02d}{minute:02d}" # Return the time in 24-hour format as a four-digit string with leading zeros if necessary

# TESTS FOR CONFIRMATIONS:
# print(convert_to_24_hour(9, 30, "am"))  
# print(convert_to_24_hour(9, 30, "pm")) 
# print(convert_to_24_hour(12, 00, "pm"))   
# print(convert_to_24_hour(12, 00, "am"))   
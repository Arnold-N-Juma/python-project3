def time_in_24hrs(hour, minute, period):
    if period.lower() == "am":  #This if statement checks if the time is set to am, if it is in am, then it doesn't add any value
        if hour == 12:
            hour = 0
    elif period.lower() == "pm": #If time is in pm it add 12 to the hour time
        if hour != 12:
            hour += 12

    time_24hrs = f"{hour:02d}{minute:02d}"  #  ensures that each number is displayed with at least two digits, adding leading zeros if needed.
    return time_24hrs

print(time_in_24hrs(11, 30, "pm"))

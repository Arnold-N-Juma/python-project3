def convert_to_24_hour(hour, minute, period):
    if period.lower() == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    # Format the hour and minute as two-digit strings
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)

    # Concatenate the formatted hour and minute to get the 24-hour time
    time_24_hour = hour_str + minute_str

    return time_24_hour

print(convert_to_24_hour(8, 30, "am"))  # Output: "0830"
print(convert_to_24_hour(8, 30, "pm"))  # Output: "2030"

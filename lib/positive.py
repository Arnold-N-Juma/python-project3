def positive(a, b, c):
    positive_count = 0  #sets the counter of the numbers as 0

    if a > 0:
        positive_count += 1  #evaluates the first number
    if b > 0:
        positive_count += 1  #evaluates the second number
    if c > 0:
        positive_count += 1  #evaluates the third number

    return positive_count == 2  #Checks the numbers if 2 are positive


print(positive(2, 4, -3))

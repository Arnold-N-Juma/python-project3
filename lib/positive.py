def positive(a, b, c):
    positive_count = 0  #sets the counter of the numbers as 0

    if a > 0:
        positive_count += 1  #evaluates the first number, if it's above 0 it adds it as a positive count
    if b > 0:
        positive_count += 1  #evaluates the second number
    if c > 0:
        positive_count += 1  #evaluates the third number

    return positive_count == 2  #Checks the numbers if 2 are positives


print(positive(11,10,-8))

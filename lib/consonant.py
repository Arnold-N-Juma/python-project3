def compute(statement):
    vowels = "aeiou"
    consonant_values = {letter: ord(letter) - ord('a') + 1 for letter in "abcdefghijklmnopqrstuvwxyz" if letter not in vowels}

    def get_consonant_value(substring):
        return sum(consonant_values[letter] for letter in substring)

    max_value = 0
    current_value = 0
    current_substring = ""

    for letter in statement:
        if letter not in vowels:
            current_substring += letter
            current_value += consonant_values[letter]
        else:
            if current_value > max_value:
                max_value = current_value
            current_value = 0
            current_substring = ""

    # Check one last time after the loop
    if current_value > max_value:
        max_value = current_value

    return max_value


print(compute("super"))   
print(compute("human"))   

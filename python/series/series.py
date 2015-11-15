def slices(string, series):

    digit_list = [int(digit) for digit in string]

    if series > len(string) or series <= 0:
        raise ValueError("Error: The sequence is larger than the string or less than 1!")

    return [digit_list[i:series + i] for i in range(len(digit_list)) if series + i <= len(digit_list)]

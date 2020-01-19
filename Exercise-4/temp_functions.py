def fahr_to_celsius(temp_fahrenheit):
    converted_temp = (temp_fahrenheit - 32) / 1.8
    return converted_temp

def temp_classifier(temp_celsius):
    if temp_celsius < 0:
        return 0
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1
    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    else:
        return 3
def is_leap(year):
    leap = False  # Initially assume it is not a leap year

    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If it is, check if it's also divisible by 100
        if year % 100 == 0:
            # If divisible by 100, it should also be divisible by 400 to be a leap year
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    return leap  # Return the result

# Example usage:
year = int(input("Enter a year: "))
print(is_leap(year))

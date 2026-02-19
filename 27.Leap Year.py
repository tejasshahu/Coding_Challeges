"""2025
point 1: Return True or False based on year is leap year or not.
point 2: Once in 400 year we get it. i.e. 2000, 2400.
point 3: 2300 is not leap year.
point 4: every 4 year we have leap year.

Test case 1: 2000 is leap year.
Test case 2: 2001 is not leap year.
Test case 3: 2500 is not leap year.
Test case 4: 2004, 2008 are leap years.
"""

def leap_year(given_year):
    if given_year % 400 == 0 or ((given_year % 4) == 0 and (given_year % 100) != 0):
        return f"Given year {given_year} is Leap Year."
    return f"Given year {given_year} is not a Leap Year."

print(leap_year(2003))

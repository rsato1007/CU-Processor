from django.shortcuts import render

# Create your views here.
# Some things to code in views.py:
# (1) only display middle initial instead of middle name
# (2) Implement rules for what member numbers are allowed:
# --Must be at least 6 digits and 9 digits max
# --Can't have numbers like 111222, 333444 (We'll figure out how to program this)
# --Maybe program something where it starts with 6 digits and increases as the number gets bigger.
# in fact my initial idea is to have the program start at the halfway point and go from there. Halves 1000 times or soemthign like that.
# There's a name for this algorithm, I know it.

# Helper functions for testMemberNumber
# first one checks for number of unique digits in member number
def uniqueDigits(str):
    counter = 0
    compareStr = ""
    for digit in str:
        if compareStr.find(digit) < 0:
            counter += 1
            compareStr += digit
        if counter == 3:
            return False
    return True

# Checks if the member number is comprised of sequential digits with
# the following format: 1234, 2345, 6789, etc.
def countUpCheck(num):
    # For this one, I am thinking of a window based pattern.
    return True

# This function is meant to test if member number meets our requirements
def testMemberNumber(num):
    result = "Pass"
    if num <= 100000 or num >= 1000000000:
        return "Fail: number out of range."
    # converts number to string
    num = str(num)
    if uniqueDigits(num):
        return "Fail: number needs more unique digits"
    if countUpCheck(num):
        return "Fail: Number is too predictable."
    return result

# Function that creates a membernumber that meets certain criteria.
def createNum():
    # Maybe this can be a while function that only breaks out once it run through the function tests
    # and has a number that meets those requirements.
    return

print(testMemberNumber(53647)) # Fail
print(testMemberNumber(111222)) # Fail
print(testMemberNumber(88888444)) # Fail
print(testMemberNumber(123456))
print(testMemberNumber(375536))
print(testMemberNumber(12345678912)) #Fail
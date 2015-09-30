#!/usr/bin/env python3

"""
Palindrome solver for 3 digits.
"""


# check if palindrome
def ispalindrome(number):
    string_of_number = str(number)
    if string_of_number[::-1] == string_of_number:
        return True
    else:
        return False


# check if biggest
def isbiggest(number, biggest_palindrome):
    if number > biggest_palindrome:
        return True
    else:
        return False
# Loop through all two three digit nums
biggest_palindrome = 0
for x in range(999, 100, -1):
    for y in range(x, 100, -1):
        product = int(x * y)
        if ispalindrome(product) and isbiggest(product, biggest_palindrome):
            biggest_palindrome = product
print(biggest_palindrome)

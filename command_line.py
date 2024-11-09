import sys
import unittest
import convert
import keyboard

# Task 3
if __name__ == '__main__':
    print(sys.argv)
#the function's purpose is to process a command line argument
#it makes sure the code is run as the main program
#the input is numbers or 'done'
#the output is a sum

if __name__ == '__main__':
    gather_list = keyboard.gather_numbers()
    total = 0.0
    for num in gather_list:
        total += num
    print("The sum of the numbers is:",total)

#when I do the tests for this, the right print statement shows up in the console
#so my tests pass
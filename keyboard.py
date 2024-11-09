from typing import Optional

import convert


# Task 2
def gather_numbers()->list[float]:
    gather_list=[]
    while True:
        numbers = input("Enter a number, or if you are done entering numbers, type 'done' in lowercase:")
        if numbers == 'done':
            break #end code
        result = convert.str_to_float(numbers)
        if result is not None:
            gather_list.append(result) #skip over the inputs that can't be converted
    return gather_list
#the function's purpose is to make a list of numbers from a user's input
#the input is entered by the user and is a series of numbers, or 'done' if they are done entering numbers
#the output is a list of float values
#the parameter can be any type
#list[float] is returned

if __name__ == '__main__':
    gather_list = gather_numbers()
    total = 0.0
    for num in gather_list:
        total += num
    print("The sum of the numbers is:",total)
#the purpose of this is to call gather_numbers and print the total sum of the numbers
#the input is gather_list
#the output is a statement saying the sum of the numbers
#the types are list[float] and float
#a statement with a float value is returned





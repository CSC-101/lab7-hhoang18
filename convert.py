from typing import Optional
# Task 1
def str_to_float(string: str)->Optional[float]:
    try:
        return float(string)
    except ValueError:
        return None
#the function's purpose is to convert a string to a float value if the string contains a float
#if a float value is not in the string, then None is returned
#the input is a string
#the output is a float or None
#the parameter is type string
#the output is type float or None






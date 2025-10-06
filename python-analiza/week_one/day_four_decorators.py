# Ex1:Hello Decorator
# 
# Write a decorator that prints "Start function" before the 
# function runs and "End function" after it finishes.

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Start function")
#         result = func(*args, **kwargs)
#         print("End function")
#         return result
#     return wrapper

# @my_decorator
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("David")

# Output:
# Start function
# Hello, David!
# End function



# Ex2: Timing Decorator
#
#  Write a decorator that measures how long a 
#  function takes to run and prints the execution time.


# import time

# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds")
#         return result
#     return wrapper



# Ex3: Logging Arguments
#  Write a decorator that prints all arguments passed 
#  to the function before it runs.

# def log_arguments(func):
#     def wrapper(*args, **kwargs):
#         print(f"Arguments: args={args}, kwargs={kwargs}")
#         return func(*args, **kwargs)
#     return wrapper



# Ex4: Uppercase Decorator
#  Write a decorator that converts
#  the return value of a function to uppercase (if it’s a string).

# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result.upper()
#         return result
#     return wrapper


# Ex5:
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


# Ex5: Count Calls
#  Write a decorator that counts how many times a function has been called.
# def count_calls(func):
#     def wrapper(*args, **kwargs):
#         wrapper.call_count += 1
#         print(f"Function '{func.__name__}' has been called {wrapper.call_count} times.")
#         return func(*args, **kwargs)
#     wrapper.call_count = 0
#     return wrapper

# @count_calls
# def greet(name):
#     return f"Hello, {name}!"    

# greet("Alice")
# greet("Bob")        


# Ex6: Authentication Check
#  Write a decorator that checks if a user has permission
#  (e.g., is_admin=True) before running the function.

# user = {"username": "alice", "is_admin": True}


# def require_admin(func):
#     def wrapper(user, *args, **kwargs):
#         if user.get("is_admin"):
#             return func(user, *args, **kwargs)
#         else:
#             print("Access denied: Admins only.")
#     return wrapper


# @require_admin
# def delete_user(user, username):
#     print(f"User '{username}' has been deleted by admin '{user['username']}'.")


# delete_user(user, "bob")


#  Ex7: Memoization Decorator
#  Write a decorator that caches the results of a function so repeated 
#  calls with the same arguments return instantly.

# def memoize(func):
#     cache = {}
#     def wrapper(*args):
#         if args in cache:
#             return cache[args]
#         result = func(*args)
#         cache[args] = result
#         return result
#     return wrapper

# @memoize    
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))


#Ex8: Retry Decorator
#  Write a decorator that retries running
#  a function up to 3 times if it raises an exception.

# def retry_decorator(func):
#     def wrapper(*args, **kwargs):
#         for attempt in range(3):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 print(f"Attempt {attempt + 1} failed: {e}")
#         print("All attempts failed.")
#     return wrapper

# @retry_decorator
# def divide(a, b):
#     return a / b

# print(divide(10, 2))
# print(divide(10, 0))




#Ex 9:Decorator with Parameters
#  Write a decorator that takes a parameter
#  (e.g., number of times to run the function)
#  and executes the function accordingly.

# def repeat_decorator(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @repeat_decorator(3)
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("David")


#Ex10: Class-based Decorator
#  Implement a decorator as a class (using __call__) 
#  that measures execution time of 
#  functions and stores the history in a dictionary.
# import time

# class TimingDecorator:
#     def __init__(self):
#         self.history = {}

#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             result = func(*args, **kwargs)
#             end_time = time.time()
#             execution_time = end_time - start_time
#             self.history[func.__name__] = execution_time
#             print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
#             return result
        
#         # Add method to access history through the wrapper
#         wrapper.get_history = self.get_history
#         return wrapper

#     def get_history(self):
#         return self.history

# # Create an instance of the decorator
# timing_decorator = TimingDecorator()

# @timing_decorator
# def example_function(n):
#     total = 0
#     for i in range(n):
#         total += i
#     return total

# @timing_decorator
# def another_function():
#     time.sleep(0.1)  # Simulate some work
#     return "Done"

# # Test the decorator
# print("Testing the TimingDecorator:")
# result1 = example_function(1000000)
# result2 = another_function()

# # Access the timing history
# print("\nTiming History:")
# history = timing_decorator.get_history()  # Access from the decorator instance
# for func_name, exec_time in history.items():
#     print(f"{func_name}: {exec_time:.6f} seconds")
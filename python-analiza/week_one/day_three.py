                  
# NameError: name 'username' is not defined
# def greet():
#     return f"Hello, {username}!"
# print(greet())

# RESULT:
# def greet(username):
#     return f"Hello, {username}!"
# print(greet("David"))




# UnboundLocalError: cannot access local variable 'count' 
# where it is not associated with a value
# count = 10
# def bump():
#     count += 1
#     return count
# print(bump())

# RESULT:
# count = 10
# def bump():
#     global count
#     count += 1
#     return count
# print(bump())





# AttributeError: 'str' object has no attribute 'push'
# text = "debugging"
# print(text.push("!"))

# RESULT:
# text = "debugging"
# print(text + "!")




# IndexError: list index out of range
# nums = [1, 2, 3]
# for i in range(0, len(nums)):
#     print(nums[i + 1])

# RESULT:
# nums = [1, 2, 3]
# for i in range(0, len(nums)):
#     print(nums[i])




# KeyError: 'username'
# config = {"host": "localhost", "port": 5432}
# print(config["username"])

# RESULT:
# config = {"host": "localhost", "port": 5432}
# print(config["host"])




# TypeError: can only concatenate str (not "int") to str
# age = "12"
# print(age + 5)

# RESULT:
# age = "12"
# print(age + "5")




# ValueError: invalid literal for int() with base 10: '12.5'
# user_input = "12.5"
# print(int(user_input))

# RESULT:
# user_input = "12.5"
# print(float(user_input))



# ZeroDivisionError: division by zero
# def ratio(a, b):
#     return a / b
# print(ratio(10, 0))


# RESULT:
# def ratio(a, b):
#     if b == 0:
#         return "Error: Division by zero is not allowed."
#     return a / b
# print(ratio(10, 0))



# FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
# with open("data.csv") as f:
#     print(f.readline())

# RESULT:
# import os

# try:
#     with open("data.csv") as f:
#         print(f.readline())
# except FileNotFoundError:
#     print("File 'data.csv' not found. Creating it now...")
#     # created a CSV file with sample data
#     with open("data.csv", "w") as f:
#         f.write("name,age,city\n")
#         f.write("David,25,Tel Aviv\n")
#         f.write("Sarah,30,Jerusalem\n")
#         f.write("Michael,28,Haifa\n")
#     print("File created successfully!")
    
#     # now read the newly created file
#     with open("data.csv") as f:
#         print("First line:", f.readline().strip())
   
   
    
# ModuleNotFoundError: No module named 'jsonn'
# import jsonn
# print(json.dumps({"ok": True}))

# RESULT:
# import json
# print(json.dumps({"ok": True}))



# RecursionError: maximum recursion depth exceeded
# def down(n):
#     return down(n - 1)
# print(down(5))

# RESULT:
# def down(n):
#     if n <= 0:
#         return "Done"
#     return down(n - 1)
# print(down(5))



# Infinite loop – loop condition never changes
# x = 5
# while x > 0:
#     print(x)
# # x never changes

# RESULT:
# x = 5
# while x > 0:
#     print(x)
#     x -= 1    



# Mutable Default Argument
# def add_item(item, bucket=[]):
#     bucket.append(item)
#     return bucket

# print(add_item("a"))
# print(add_item("b"))

# RESULT:
# def add_item(item, bucket=None):
#     if bucket is None:
#         bucket = []
#     bucket.append(item)
#     return bucket
# print(add_item("a"))
# print(add_item("b"))




# Late binding in closures – all functions print same value
# funcs = []
# for i in range(3):
#     funcs.append(lambda: print(i))

# for f in funcs:
#     f()  # Expected 0,1,2; what happens?
#    # Prints: 2 2 2



# # RESULT:
# funcs = []
# for i in range(3):
#     funcs.append(lambda i=i: print(i))

# for f in funcs:
#     f()  # Prints: 0 1 2



# Modifying a list while iterating – skipped elements
# items = [1, 2, 3, 4, 5]
# for x in items:
#     if x % 2 == 0:
#         items.remove(x)
# print(items)

# RESULT:
# items = [1, 2, 3, 4, 5]
# for x in items[:]:
#     if x % 2 == 0:
#         items.remove(x)
# print(items)



# TypeError: 'list' object is not callable
# Shadowing a builtin – unexpected errors later
# list = [1, 2, 3]
# print(list( ("a", "b") ))

# RESULT:
# my_list = [1, 2, 3]
# print(list( ("a", "b") ))



# Missing import – using a module without importing it
# import logging
# logging.debug("Start")   # Why no output?

# RESULT:
# import logging
# logging.basicConfig(level=logging.DEBUG)  
# logging.debug("Start")   # Now it works



# Wrong operator precedence – logic bug, no exception
# a, b, c = True, False, True
# if a and b or c == True:
#     print("Pass")
# else:
#     print("Fail")

# # RESULT:
# a, b, c = True, False, True
# if a and (b or c):
#     print("Pass")
# else:
#     print("Fail")




# f-string with missing variable – runtime NameError
# name = "Avi"
# print(f"User: {full_name}")

# RESULT:
# name = "Avi"
# print(f"User: {name}")



# Off-by-one in range – last element never processed
# data = [10, 20, 30, 40]
# total = 0
# for i in range(len(data) - 1):
#     total += data[i]
# print("Total:", total)  # Why is 40 missing?

# RESULT:
# data = [10, 20, 30, 40]
# total = 0
# for i in range(len(data)):
#     total += data[i]
# print("Total:", total)
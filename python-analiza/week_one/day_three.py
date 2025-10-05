                  
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

                  
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
user_input = "12.5"
print(float(user_input))
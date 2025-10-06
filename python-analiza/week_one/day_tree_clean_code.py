# Meaningful Names
# def f(a, b):
#     return a / (b * 60)

# print(f(120, 2))

# RESULT:
# def calculate_speed_kmh(distance_km, time_hr):
#     return distance_km / ( time_hr * 60)

# print(calculate_speed_kmh(120, 2))





# Magic Numbers
# def area(r):
#     return 3.14159 * r * r

# print(area(5))

# RESULT:
# def area(radius):
#     PI = 3.14159
#     return PI * radius * radius

# print(area(5))





# Duplicated Code
# def print_user1(name, age):
#     print("User:", name)
#     print("Age:", age)

# def print_admin_user(name, age):
#     print("User:", name)
#     print("Age:", age)


# RESULT:
# def print_user(name, age):
#     print("User:", name)
#     print("Age:", age)

# def print_admin_user(name, age):
#     print_user(name, age)        




# Long Function
# def process_user(data):
#     name = data[0]
#     age = data[1]
#     print("User:", name)
#     if age < 18:
#         print("Minor")
#     else:
#         print("Adult")
#     if age >= 65:
#         print("Senior")

# process_user(("Alice", 70))

# RESULT:

# def print_user(name, age):
#     print("User:", name)
#     print("Age:", age)

# def age_group(age):
#         if age < 18:
#             return "Minor"
#         elif age >= 65:
#             return "Senior"
#         else:
#             return "Adult"
        
# def process_user(name, age):
#   print_user(name, age)
#   age_group(age)




# Inconsistent Formatting & Poor Readability
# def calc(x,y):return x+y;print(calc(2,3))

# RESULT:
# def calc(x, y):
#     return x + y
# print(calc(2, 3))


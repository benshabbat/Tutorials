                  
# NameError: name 'username' is not defined

# def greet():
#     return f"Hello, {username}!"
# print(greet())


def greet(username):
    return f"Hello, {username}!"
print(greet("David"))

# UnboundLocalError: cannot access local variable 'count' 
# where it is not associated with a value
# count = 10
# def bump():
#     count += 1
#     return count
# print(bump())


count = 10
def bump():
    global count
    count += 1
    return count
print(bump())

name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

length = len(name)
index = name.find(" ")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha()
result = phone_number.count(" ")
phone_number = phone_number.replace("-", "")
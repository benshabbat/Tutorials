# if = Do some code IF condition is True
# else = Do something else if above condition/s are False

age = int(input("Enter your age: "))

if age >= 100:
   print("You are too old to sign up")
elif age >= 18:
   print("You are now signed up")
elif age < 0:
   print("You haven't been born yet")
else:
   print("You must be 18+ sign up")


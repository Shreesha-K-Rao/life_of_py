#1 📌 Purpose: Printing a beautiful multi-line welcome message in Kannada.

print("""Devare,Nimage Hrutpurvaka Namaskaragalu! 
Indininda Nanu Python Programing Language Kalibeku anta Dhrudavaada Manassannu Madiddene. 
Dayavittu Nimma Ashirvaada&Krupe nanna meleirali,
yendu Hrudpurvaka Prarthane!!!
inthi nimma preethiya shishya, 

      ~ Shreesha Krishna Rao""")

# Explanation:

# Using triple quotes (""") to print multiple lines together.
# No need for \n explicitly when using triple quotes.

# --------------------------------------------------------------------------------------------#

#2 📌 Purpose: Creating variables of different types and checking their types.

age = 25       # Integer value
price = 19.95  # Float value
name = "Shreesha"  # String value
is_coding = True   # Boolean value

print(age, type(age))            # Prints value and its type
print(price, type(price))        
print(name, type(name))          
print(is_coding, type(is_coding))

#Explanation:

# type() function shows the data type of the variable.
# Python dynamically assigns data types.

# --------------------------------------------------------------------------------------------#


#3 📌 Purpose: Taking input from user, converting types, and printing output.

name = input("May I know your name please?") 
age = int(input("That's Awesome! May I get to know how old you are?"))
fav_num = int(input("Interesting! What's your lucky number?"))

print(f"Hello {name}, You are a {age} year old amazing person and your lucky number is: {fav_num}")
print('\n')  # To give a line space
print("A Cool Note to you is - ")

#Print a message based on the user's age.

if age < 30:
    print("You are an awesome young adult who has a lot to do in life!")
elif 30 <= age <= 50:
    print("You have done a lot! Time to take rest now.")
elif 50 <= age <= 60:
    print("Transitioning from being a young person to an older person. Don't worry about transitioning! Be young and smiling always!")
elif 60 <= age <= 80:
    print("Recreate the things which you have enjoyed.")
else:
    print("Relive every single moment, as you won't get this life back again!")

# Explanation:

# input() reads a string by default.
# int() converts input to integer.
# f-string used for clean string formatting.
# if-elif-else blocks are used for multiple conditions.
# Conditions checked sequentially until the first match.

# --------------------------------------------------------------------------------------------#


#4 📌 Purpose: Based on age, give advice on operating a machine.

age = int(input("What's your age?"))

if age < 10:
    print("You are too young to operate this machine")
elif 11 <= age <= 30:
    print("You are at the right age to operate this machine")
elif 31 <= age <= 50:
    print("You have to upskill a lot to operate this machine")
elif 51 <= age <= 60:
    print("You should probably be just monitoring this machine by now, no need to work, just relax and tune your juniors!")
else:
    print("You are a retired person, Please take care of your amazing life ahead")

# Explanation:

# Real-life based conditions created for better understanding.

# --------------------------------------------------------------------------------------------#

#5 📌 Purpose: Perform basic mathematical operations between two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n")  # Just for spacing
print("Addition of two numbers is:", a + b, "\n")
print("Subtraction of two numbers is:", a - b)
print("Multiplication of two numbers is:", a * b)
print("Division of two numbers is:", a / b)
print("Mod of two numbers is:", a % b)
print("Power of two numbers is:", a ** b)

# Explanation:

#   + addition
#   - subtraction
#   * multiplication
#   / true division
#   % modulus (remainder)
#   ** exponentiation (power)


#6 📌 Purpose: Create a simple calculator that does selected operations.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose any operation which you want to operate - Addition, Subtraction, Multiplication, Division")
operation = input("")

if operation == "Addition":
    print("Result is:", num1 + num2)
elif operation == "Subtraction":
    print("Result is:", num1 - num2)
elif operation == "Multiplication":
    print("Result is:", num1 * num2)
elif operation == "Division":
    print("Result is:", num1 / num2)
else:
    print("Invalid Operation, Please try again with the options mentioned only! :)))")

# Explanation:

# Dynamic input and operation selection.
# Clean error handling for invalid operations.
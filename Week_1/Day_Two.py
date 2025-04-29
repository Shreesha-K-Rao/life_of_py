#1 – Understanding How Decisions Are Made in Python

age = int(input("Please enter your age! : "))
if age < 18 : 
    print("You are a minor, You can't enter in")
elif 19 <= age <= 60 :
    print("You are a right person age to enter this place, Hearty Welcome! :)")
else :
    print("You are a senior citizen, We handle you with care! You are most welcome to our place! :)))")

# -------------------------------------------------------------------------------------------------------- #


#2 – Even, Odd, Zero, or Negative Number Detection

x = int(input("Enter any number : "))

if x > 0 and x%2==0:
    print("Hurray, it's a even number!")
elif x>0 and x%2!=0:
    print("Uh, it's an odd number!")
elif x==0:
    print("Uhuh! No Zero's please!")
else:
    print("Sorry, No Negative Numbers Please!!!")

# -------------------------------------------------------------------------------------------------------- #


#3 – User ID and Password Authentication (Basic)

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == "admin" :
    if password == "123456" :
        print("Login Successful! Welcome Home :) ")
    else :
        print("Login Unsuccessful! Please try again : ")
else: 
    print("Unknown User, Please Contact the admin for further support")


#4 – Grade Checker Based on Marks

marks = int (input("Please enter the marks that the respective student has scored : "))

if 85<= marks <=100 :
    print(f"The student has scored {marks} marks, A Grade!!! Keep it Up and Be Consitent. ")
elif 70<= marks <85 :
    print(f"The student has scored {marks} marks, B Grade. Please work hard and be perfect next time!")
elif 45<= marks <70 :
    print(f"The student has scored {marks} marks, C Grade! Must work harder and perform well next time! ")
elif marks <45 :
    print(f"The student has scored {marks} marks, D Grade!! Must work hard, else strict action will be taken.")
else : 
    print("Please enter a valid number!")

#5 – Even and Divisible by 4 Checker

num = int(input("Enter a Number : "))

if num>0 and num%2==0:
    if num%4==0 :
        print("Hurray! The Number is Even and is Divisble by 4! ")
    else :
        print("Ohoh! The Number is Even But is Not Divisble by 4! ")
elif num==0:
    print("No Zeros Please")
elif num<0:
    print("No Negatives Please! ")
else:
    print("Odd Number!") 
    

#6 – Login System with Limited Attempts (Challenge)

attempts = 0
max_attempts=3

while attempts < max_attempts :
    username = input("Please enter your username : ")
    password = input("Please enter your password : ")

    if username == "admin":
        if password == "rajbshett@123":
            print("Logged in Succesfully!")
            break
        else :
            print("Please enter the right password, Login Unsuccesful!")
            attempts+=1
    else : 
        print(f"Incorrect Username!")

    attempts += 1
    attempts_left = max_attempts - attempts

    if attempts > 0:
        print(f"You have {attempts_left} attempts left to login! Else it'll be blocked and you need to contact the admin.\n")


if attempts == max_attempts :
    print("Account Locked, Contact Admin for Further Queries! ")
    



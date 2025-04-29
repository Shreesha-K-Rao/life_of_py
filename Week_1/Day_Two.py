#1 Understand how decisions are made in Python.
# age = int(input("Please enter your age! : "))
# if age < 18 : 
#     print("You are a minor, You can't enter in")
# elif 19 <= age <= 60 :
#     print("You are a right person age to enter this place, Hearty Welcome! :)")
# else :
#     print("You are a senior citizen, We handle you with care! You are most welcome to our place! :)))")


#2 Getting to know a number is even or odd zero negative number 

x = int(input("Enter any number : "))

if x > 0 and x%2==0:
    print("Hurray, it's a even number!")
elif x>0 and x%2!=0:
    print("Uh, it's an odd number!")
elif x==0:
    print("Uhuh! No Zero's please!")
else:
    print("Sorry, No Negative Numbers Please!!!")

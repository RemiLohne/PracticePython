'''
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an 
even / odd number react differently when divided by 2?

Extras:
1    If the number is a multiple of 4, print out a different message.

2    Ask the user for two numbers: one number to check (call it num) and one 
     number to divide by (check). If check divides evenly into num, tell that 
     to the user. If not, print a different appropriate message.
'''


num = int(input("Enter a number : "))
divide = num % 2 

if divide == 0 :
    print("You entered  ",num," :This number is even")
elif divide != 0 :
    print("You entered ",num," :This number is odd")
else : 
    print("I have no idea what you are trying to do")

# Extras 1 :
multiper = num % 4
if multiper == 0 :
    print (num," :This number is multiple of 4")
    
# Extras 2 : 
check = int(input("\nEnter number 2 : "))
if num % check == 0 : 
    print(num, ": this number divides evenly by", check)
else:
    print(num, ": this number does not evenly divde by", check)


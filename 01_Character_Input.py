'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will 
turn 100 years old.

Extras:
1    Add on to the previous program by asking the user for another number 
     and printing out that many copies of the previous message. 
     (Hint: order of operations exists in Python)
     
2    Print out that many copies of the previous message on separate lines. 
     (Hint: the string "\n is the same as pressing the ENTER button)
 '''

name = input("Enter your name : ")
age = input("Enter your age : ")
text = "Your name is : " + name + "\nAnd you are : "+ age + " years old\n\n"
print(text)
nr = int(input("enter a number : "))
print(text * nr)
    

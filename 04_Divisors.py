# coding: iso-8859-1
'''
Create a program that asks the user for a number and then prints out a 
list of all the divisors of that number. If you don't now what a divisor is, 
it is a number that divides evenly into another number. For example, 
13 is a divisor of 26 because 26 divided 13 has no remainder
'''

x = range(2, 11)
num = 0 
num = int(input("Enter a number : "))
divisible = []

for i in x:
    calc = num % i
    if calc == 0:
        divisible.append(i)
        
print (num," is even divisible with followin numbers :", divisible)

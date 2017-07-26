'''
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that 
are common between the lists (without duplicates). Make sure your program works
on two lists of different sizes.

Extras:

1     Randomly generate two lists to test this

2    Write this in one line of Python (don’t worry if you can't figure this out
     at this point - we’ll get to it soon)
'''
import random


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = a + b 
new_list = []
for i in c:
    if i not in new_list:
        new_list.append(i)
print(new_list)

#extra 1         
list1= random.sample(range(1, 101), 10)
list2= random.sample(range(1, 101), 10)
random_list = list1 + list2
new_list2 = []
for y in random_list:
    if y not in new_list2:
        new_list2.append(y)
print(new_list2)

#extra 2 

# example without list comprehension
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

# same example as above using list comprehension
new_list = [n + 1 for n in numbers]

print(new_list)

# another example of List Comprehension
name = "Cleiton"
new_list = [n for n in name]
print(new_list)

# challenge of list Comprehension, using the range to create a list with the double of the value
result = [x * 2 for x in range(1,5)]
print(result)

# another example using conditionals to create a list using List Comprehensions
names = ["Angela", "Beth", "Deise", "Erica", "Daniella"]
result = [name.upper() for name in names if len(name) < 6]
print(result)

#Exercise 1
#You are going to write a List Comprehension to create a new
# list called squared_numbers. This new list should
# contain every number in the list numbers but each number should be squared.

#e.g. 4 * 4 = 16
#4 squared equals 16.
#DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.
#Target Output
#[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆
# Write your 1 line code 👇 below:
squared_numbers = [square * square for square in numbers]
# Write your code 👆 above: print(squared_numbers)


#Exercise 2
# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.
# First, use list comprehension to convert the list_of_strings to a list of integers.
# Then use list comprehension again to create a new list called result. This new list should only contain the even numbers from the list numbers.
# Again, try to use Python's List Comprehension instead of a Loop.
list_of_strings = input().split(',')
# 🚨 Do not change the code above
# TODO: Use list comprehension to convert the strings to integers 👇:
list_of_integers = [eval(number) for number in list_of_strings]
# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [num for num in list_of_integers if num%2==0]
# Write your code 👆 above:
print(result)


#Exercise 3
#Finding the duplicate values between 2 files .txt using list comprehension:
with open("file1.txt", mode="r") as file:
    list1 = file.readlines()
with open("file2.txt", mode="r") as file:
    list2 = file.readlines()
result = [int(num) for num in list1 if num in list2]
# Write your code above 👆
print(result)


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
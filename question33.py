'''
Question:
Define a function which can generate and print a list
where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
'''

def super_function():
    li = list()
    for item in range(1, 21):
        li.append(item ** 2)
    return li

print super_function()
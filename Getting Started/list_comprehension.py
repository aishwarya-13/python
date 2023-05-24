"""
List comprehension offers a shorter syntax when you want to create a new list based 
on the values of an existing list.
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)
print(newList)

"""
With list comprehension you can do all that with only one line of code:
"""
newlist = [x for x in fruits if "a" in x]
print(newlist)

"""
Create a list of list that contains the words uppercase,lowercase version and length of the word
"""
words = ['Hi', 'i', 'am', 'aishwarya', 'vhatkar']
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)
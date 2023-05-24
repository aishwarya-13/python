"""
Function arguments and parameters
"""
def about(name, age, likes = 'Python'): #These are function parameters
    sentence = 'Meet {}! They are {} years old and they like {}'.format(name, age, likes)
    return sentence
print(about('Jack', 30, 'Javscript')) #These are function arguments
print(about(age = 40, name = 'Jill', likes = 'Java')) #These are function arguments
print(about('Jeanine', 20))

"""
Packing and unpacking arguments
"""

#unpacking
mylist = [1,2,3,4,5]
print(mylist) #[1, 2, 3, 4, 5]
print(*mylist) #1 2 3 4 5

a = 'hello'
print(a) #hello
print(*a) #h e l l o

#Packing
def add(*numbers):
    total = 0
    for num in numbers:
        total+= num
    return total

print(add(5, 10))
print(add(1,2,3,4,5,10))

"""
Unpack Dictionaries
"""
def about(name, age, likes):
    return "Meet {}! They are {} old and likes {}".format(name, age, likes)

dicti = {
    "age": 30,
    "name": "Aishwarya",
    "likes":"Python"
}
print(about(**dicti))

def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))

foo(aish = "Female", rohit = "Male") #aish:Female rohit:Male
foo(aish = "Female", rohit = "Male", ojas = "Male") #aish:Female rohit:Male ojas:Male
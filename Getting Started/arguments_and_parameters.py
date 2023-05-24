"""
Function arguments and parameters
"""
def about(name, age, likes = 'Python'): #These are function parameters
    sentence = 'Meet {}! They are {} years old and they like {}'.format(name, age, likes)
    return sentence
print(about('Jack', 30, 'Javscript')) #These are function arguments
print(about(age = 40, name = 'Jill', likes = 'Java')) #These are function arguments
print(about('Jeanine', 20))

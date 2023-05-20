# Asking the user for input
# Ask user for name
name = input("What is your name?")
print(name)
print(type(name))

# Ask user for age
age = input("How old are you?")
print(age) # 30
print(type(age)) #<class 'str'>

#Ask user for city
city = input('What city do you live?')

#Ask user what they enjoy?
love = input("What do you love doing?")

#Create output text
output = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = output.format(name, age, city, love)
print(output)
""""
#Type coercion not done in Python
d = 'nice'
e = 1
#print(d + e) # TypeError: can only concatenate str (not "int") to str
#^^Convert number to string using str() 
#print(d + str(e))#Convert number to string
#^^format() -> No need to convert number to string explicity. It automatically converts
print("{}-{}".format(d,e))
print("{1}-{0}".format(d,e)) #placing e first and d second

#String Concatenation
a = 'Hello'
b = 'World!'
c = a + ' ' + b
#print(c) # Hello World!
#printing a string multiple times
#print(a * 4) # HelloHelloHello

"""

"""
name = "Aishwarya"
#print(name)
#print(type(name)) # <class 'str'>

message = 'Ojas said to me "I will see you later"'

# Include the string in 3 double quotes OR 3 single quotes
lorem = '''Lorem Ipsum is simply dummy text of 
the printing and typesetting industry. 
Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, 
when an unknown printer took a galley of 
type and scrambled it to make a type 
specimen book. It has survived not only 
five centuries, but also the leap into 
electronic typesetting, remaining 
essentially unchanged.'''
#print(lorem)
"""
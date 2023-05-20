# String methods

# Count the number of chars or word in the string
print('hello'.count('e')); # 1
print('hello'.count('a')); # 0
print('happy birthday'.count('day')) # 1

# Upper and lower case
a = 'Aishwarya'
b = 'aishwarya'
print(a.lower()) # aishwarya
print(b.upper()) # AISHWARYA
#Strings are immutable. You cannot change them unless you overwrite them
print(a)
print(b)

#Turn only  the first letter to uppercase of the string
print('aishwarya'.capitalize()) # Aishwarya

#Turn first letter of every word to uppercase
print('aishwarya vhatkar'.title()) # Aishwarya Vhatkar

# Check for uppercase / lowercase
print('aishwarya vhatkar'.isupper()) # False
print('Aishwarya'.islower()) # False

# Is everything in the string letters
print('aishwarya'.isalpha()) # True
print('aishwarya vhatkar'.isalpha()) # False

# Is string alphanumeric
print('aish123'.isalnum())

# Is all chars numbers
print('1234'.isdigit()) #True

# Search
print('aishwarya vhatkar'.index('a')) #0
print('aishwarya vhatkar'.index('ai')) #0
#print('aishwarya vhatkar'.index('zas')) #ValueError: substring not found
print('aishwarya vhatkar'.find('azz')) #-1

#Strip
print('00000aishwarya vhatkar0000'.strip('0')) #aishwarya vhatkar
print('00000aishwarya vhatkar0000'.lstrip('0')) #aishwarya vhatkar0000
print('00000aishwarya vhatkar0000'.rstrip('0')) #00000aishwarya vhatkar
#trims spaces at start and end
print('  aishwarya   '.strip()) #aishwarya

#Slice
word = 'supercaliforniaandduperchicago'
print(word[0]) #s
print(word[3]) #e
#Slice variable[start:end:step]
print(word[0:5:1]) #super
print(word[0:5:2]) #spr
print(word[5:9:1]) #cali
#slice from start to end - specify only the start
print(word[5:]) #californiaandduperchicago
#slice from start to end in steps of 2 - not specifying the end
print(word[5::2]) #clfriadueciao
#Specify only the end index - it slices from start to end
print(word[:7])
#Count from the end
print(word[-2]) #g
#using indexes dynamically
print(word[word.index('cali'): word.index('and')]) #california

#Reverse a string
#print('aishwarya vhatkar'[::-1]) #raktahv ayrawhsia





""""
#===========================

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
#Type coercion not done in Python
d = 'nice'
e = 1
#print(d + e) # TypeError: can only concatenate str (not "int") to str
#^^Convert number to string using str() 
#print(d + str(e))#Convert number to string
#^^format() -> No need to convert number to string explicity. It automatically converts
print("{}-{}".format(d,e))
print("{1}-{0}".format(d,e)) #placing e first and d second

#===========================

#String Concatenation
a = 'Hello'
b = 'World!'
c = a + ' ' + b
#print(c) # Hello World!
#printing a string multiple times
#print(a * 4) # HelloHelloHello

#===========================

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
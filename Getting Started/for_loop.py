"""
Print numbers from 1 to 9
"""
for number in range(1,10):
    print(number)

"""
Iterating a list
"""
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

"""
Iterating a string
"""
for char in "How are you?":
    print(char)

"""
Count the vowels and consonants in a string
"""
str = 'aeiou'
vowels = 0
consonants = 0

for char in str:
    if char.lower() in 'aeiou':
        vowels+=1
    elif char == " ":
        pass
    else:
        consonants+=1

print('There are {} vowels in the string'.format(vowels))
print('There are {} consonants in the string'.format(consonants))

"""
Iterating a dictionary
Print the names who have letter a in them
"""
employees = {
    "male":["Rohit", "Ryan", "Ojas", "Priyansh"],
    "female":["Aishwarya", "Shreya", "Kshiti", "Sana", "Moire"]
}
for key in employees:
    for emp in employees[key]:
        if 'a' in emp:
            print(emp)


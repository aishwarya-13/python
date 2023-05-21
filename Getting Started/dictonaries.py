"""
Similar to map/objects in JS
There is no order
CREATE a dictionary
"""
students = {
    "Aish":30,
    "Rohit":32,
    "Ojas":29,
    "Natasha":5,
    "Ryan":2
}

print(students["Aish"]) #30

"""
ADD an element in dictionary
"""
students["Fred"] = 50
print(students["Fred"]) #50

"""
DELETE an element in dictionary
"""
del students["Fred"]
print(students) #{'Aish': 30, 'Rohit': 32, 'Ojas': 29}

"""
KEYS of the dictionary
The keys are not iterable so convert it to list
"""
print(students.keys()) #dict_keys(['Aish', 'Rohit', 'Ojas'])
#print(students.keys()[0]) #TypeError: 'dict_keys' object is not subscriptable
keys_list = list(students.keys())
print(keys_list[0]) #Aish

"""
VALUES of the dictionary
"""
values_list = list(students.values())
print(values_list) #[30, 32, 29]

"""
A little complicated dictionary:
<string:list>
<string:dictionary>
"""
enhanced_students = {
    "Aish":["ID001", 30, 'A+'],
    "Rohit":["ID002", 32, 'A+'],
    "Ojas":["ID003", 29, 'A'],
    "Natasha":["ID004", 12, 'A++'],
    "Ryan":["ID005", 17, 'A++']
}

#Get details of Natasha
print(enhanced_students["Natasha"]) #['ID004', 12, 'A++']['ID004', 12, 'A++']
#Get id and age of Natasha
print(enhanced_students["Natasha"][0]) #ID004
print(enhanced_students["Natasha"][0:2]) #['ID004', 12]

optimized_students = {
    "Aish":{"ID":"ID001", "age":30, "grade":'A+'},
    "Rohit":{"ID":"ID002", "age":32, "grade":'A+'},
    "Ojas":{"ID":"ID003", "age":29, "grade":'A+'},
    "Natasha":{"ID":"ID004", "age":12, "grade":'A++'},
    "Ryan":{"ID":"ID005", "age":17, "grade":'A++'}
}

#Get details of Ryan
print(optimized_students["Ryan"]) #{'ID': 'ID005', 'age': 17, 'grade': 'A++'}
#Get age of Ryan
print(optimized_students["Ryan"]["age"]) #17
#Get grade and age of Aish
print(optimized_students["Aish"]["grade"], optimized_students["Aish"]["age"]) #A+ 30

"""
Functionas are made by defining them.
'def' keyword -> it means we are defining a function
'add' is the function name
parameters are inside the brackets
"""
def add(x, y):
    return x + y

ans = add(2,3)
#print(add(2,3))
print(ans)

"""
Reverse a string
"""
word = 'aish'
def rev(s):
    return s[::-1]
print(rev(word))

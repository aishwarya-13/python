# ! operator
print(not True)
print(not False)
print(not 2 < 3)

# Using not in if condition
x = 10
y = 20

if not y < x:
    print('It worked')

#===============================
# AND operator
c = 10
d = 5

if c >= 10 and d > 1:
    print('It worked baby')

#Using and and not operators
if not(c > 10 and d > 1):
    print('It worked !!')

#===============================
#OR operator
e = 5
f = -1

if e > 1 or f >0:
    print('Yo it worked')

#Using or and not operators
if not(e > 10 or f >0):
    print('yo yo it worked')

#==============================
g=6
f=2
if (c > 5 and d > 5) or (c > 1 and d > 1):
    print('Ummm worked')

if not ((c > 5 and d > 5) or (c > 1 and d > 1)):
    print('Ummm worked yes')
else:
    print('Did not work')
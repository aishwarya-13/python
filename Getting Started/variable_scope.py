"""
Two types of scope in python
1] Global
2] Local scope: functions create local scopes inside them
  Local variable takes priority over global variables
  Local variables are destroyed after function is done executing
"""

"""
Global scope
"""
a = 100 #global variable
d = 2 #global variable

def fun1():
    c=1 #local variable
    d=20 #local variable with same name as global variable d
    print(a)
    print(c)
    print(d)

def fun2():
    d = 100 #local variable with same name as global variable d
    print(a)
    #print(c) #NameError: name 'c' is not defined
    print(d)

print(d)
fun1()
fun2()

"""
Local scope
"""

def fun3():
    a=200
    print(a)

fun3()

"""
Two types of scope in python
1] Global
2] Local scope: functions create local scopes inside them
->Local variable takes priority over global variables
->Local variables are destroyed after function is done executing
->Python does not let you change the value of global variable. So what it does is, it creates a local variable
"""

"""
Global scope
"""
a = 100 #global variable
d = 2 #global variable

def fun1():
    c=1 #local variable
    d=20 #trying to change the value of global variable but Python does not let you change the value of global variable
    print(a)
    print(c)
    print(d)

def fun2():
    d = 100 #trying to change the value of global variable but Python does not let you change the value of global variable
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

"""
How to change global variable value in function
"""
val = 1000

def fun4():
    global val
    val = 1
    print('Changed value of global variable::::', val)

def fun5():
    print('value of global in fun5()::::',val)

print('Global variable::::', val)
fun4()
fun5()

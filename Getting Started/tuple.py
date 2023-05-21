"""
Tuples are iterable data types
We can iterate, slice the tuple just like lists
Only difference between lists and tuple is tuple cannot be changed once it is created (just like strings are immutable) while lists can be changed
When to use tuples? When you dont want to change the data accidentally and protect it.
"""

"""
Create tuple
"""
mytuple = 1,2,3,'a','b'
print(mytuple) #(1, 2, 3, 'a', 'b')
print(type(mytuple)) #<class 'tuple'>

mytuple2 = (10,20,30,'a','b','c')

"""
Tuple is immutable
"""
mylist = [1,2,3,4]
mylist[2] = 300
print(mylist) #[1, 2, 300, 4] list can be mutated

#mytuple2[2] = 300 #TypeError: 'tuple' object does not support item assignment

"""
Convert other data structure into tuple
"""
a = [1,2,3]
print(tuple(a)) #(1, 2, 3)

"""
Assigning tuple to multiple variables
Same can be done for strings and lists also
"""
(l,m,n) = (1,2,3)
print(l) #1
print(m) #2
print(n) #3

o,p,q = [10,20,30]
print(o) #10
print(p) #20
print(q) #30

x,y,z = 'abc'
print(x) #a
print(y) #b
print(z) #c
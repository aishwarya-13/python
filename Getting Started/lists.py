#Check if element exists in mylist
mylist = [1,2,3,4,5,6,7]
print(2 in mylist) #True
print(10 in mylist) #False

# ^^Add elements in mylist
mylist = mylist + [8,9,10]
mylist = mylist + ['hi']
print(mylist) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hi']
# ^^Works on iterable only. String is iterable so it will work. Will not work for integer
mylist = mylist + list('ABCD')
#mylist = mylist + list(90) #TypeError: 'int' object is not iterable
print(mylist) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hi', 'A', 'B', 'C', 'D']
#^^Add elements at specific index
mylist.insert(2,1000)
print(mylist) # [1, 2, 1000, 3, 4, 5, 6, 7, 8, 9, 10, 'hi', 'A', 'B', 'C', 'D']



"""
# ^^append will add to the end of the mylist
mylist.append(8)
"""


"""
# ^^Remove from mylist - removes 1st occurrence
# ^^In remove() we have to specify the element
print(mylist.remove(4))
print(mylist) # [1, 2, 3, 5, 6, 7]
# ^^Removing using index - useful when there are multiple ocurrences of an element
del mylist[0]
print(mylist) #[2, 3, 4, 5, 6, 7]
# ^^slice a part of mylist
del mylist[0:2]
print(mylist)
"""


"""
#Create mylists and access parts of mylists

mylist = [1,2,3,-1]
print(mylist)
print(type(mylist))

mylist2 = ['Aish', 30, True, 'hi', [1,2,3,4,5,6]]
print(mylist2) # ['Aish', 30, True, 'hi', [1,2,3,4,5,6]]
print(mylist2[2]) #True
# Can iterate from back as well
print(mylist2[-2]) #hi
print(mylist2[-1]) #[1,2,3,4,5,6]
print(mylist2[-1][0]) #1 
#Getting part of mylist from 0 to end
print(mylist2[-1][0:]) #[1,2,3,4,5,6]
#Getting part of mylist from 1 to 2 included and 3 excluded
print(mylist2[-1][1:3]) #[2, 3]
##Getting part of mylist from 1 to 5 with step 2
print(mylist2[-1][1:5:2]) #[2, 4]

"""



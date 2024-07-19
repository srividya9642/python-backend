''' in python lists are mutable that means once we create a list we can do modifications in the list
lists are used to store multiple items in a single variable, lists are one of 4 built-in data types used to store collections of data,the other
3 are Tuple, Set, and Dictionary, all with different qualities and usage.
lists are created using square brackets:'''

# creating a list
l = ["apple","banana","cherry"]
print(l)


''' list items are ordered,changeable,and allow duplicate values.
list items are indexed,the item has index[0], the second item has index[1] etc..'''


# allow duplicates
# list allows duplicate values
l = ["apple","banana","cherry","apple"]
print(l)


# list length
# to determine how many items a  list has,use the len() function:

l = ["apple","banana","cherry"]
print(len(l))


# list items-data types
# list items can be of any data types
list1 = ["apple","banana","cherry"]
list2 = [1,2,3,5,6]
list3 = [True,False,False]


# a list can contain  different data types:
list1 = ["apple",34,True,49,"hello"]

# from python's perspective ,lists are defined as object with the data type 'list':
#<class 'list'>

my_list = ["apple","banan","cherry"]
print(type(my_list))


# the list() constructor
# it is also possible to use the list() constructor when creating a new list.abs
# using a list constructor to make a list:
 
thislist = list(("apple","banna","cherry")) # note that double rounded brackets
print(thislist) 



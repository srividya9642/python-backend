# craeting a empty tuple
'''Tuple1 = ()
print("initial empty tuple: ")
print(Tuple1)

# creating a tuple with the use of string
Tuple1 = ("Geeks", 'for')
print("\n tuple with the use of string")
print(Tuple1)

#  creating tuple with the use of list
list1 = [1,2,3,4,5]
print("\n tuple with the use of lsit")
print(list1)

# creating tuple with the use of built-in function
tuple1 = tuple("geeks")
print("/n tuple with the use of function")
print(tuple1)



# creating tuple with the use of mixed data types
tuple1 = (5,'welcome',7,'geeks')
print("\n tuple with mixed data types")
print(tuple1)

# creating tuple with nested tuples
tuple1 = (0,1,2,3,4,)
tuple2 = ('python','geek')
tuple3 = (tuple1, tuple2)
print("\n tuplwith nested tuples ")
print(tuple3)

# creating a tuple with repitition
tuple1 =('geeks',) * 3
print("\n tuple with repetitions:")
print(tuple1)

# creating tuple with the use of loop
tuple1 = ('geeks')
n = 5
print("\n tuple with a loop")
for i in range(int(n)):
    tuple1 = (tuple1,)
    print(tuple1)
    
    
 # python tuple operations
 # accessing of tuples
Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple1[0])

# tuple unpacking
tuple1 = ("geeks","for","geeks")

# this line unpack
# values of tuple1
a,b,c = tuple1
print("\n values after unpacking: ")
print(a)
print(b)
print(c)'''

# concatination of tuples
tuple1 = (0,1, 2, 3)
tuple2 = ('geeks', 'for', 'geeks')

tuple3 =  tuple1 + tuple2
# printing first tuple
print("tuple1: ")
print(tuple1)

# printing second tuple
print("\ntuple2: ")
print(tuple2)

# printing final tuple
print("\n tuples after concatination: ")
print(tuple3)


       
    
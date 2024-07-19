x = 5
y = 10
print(bool(x==y))

# return false as x is none
x =  None
print(bool(x))

# return false as x is empty sequence
x = ()
print(bool(x))

# returns false as x is empty mapping
x = {}
print(bool(x))

# returns false as x is o
x = 0.0
print(bool(x))

# returns true as x is non empty string
x = "good morning"
print(bool(x))

# Boolean value from the expression
a = 10
b = 20
print(a==b)

# integers and floats as booleans
var1 = 0
print(bool(var1))

var2 = 1
print(bool(var2))

var3 = -9.7
print(bool(var3))

# boolean operators

# boolean OR
a = 1
b = 2
c = 4

if a>b or b<c:
    print(True)
else:
    print(False)
    
if a or b or c:
    print("atleast one number has boolean value as True")   
    
# boolean AND
a = 1
b = 2
c = 4
if a>b and b<c:
    print(True)
else:
    print(False)
if a and b and c:
    print("atleast one number has boollean as false" )
    
# boolean NOT
a = 0
if not a:
    print("boolean value of a is false")    
    
# boolean equivalent and not-eqivalent operator
a = 0
b = 1
if a==0:
    print(True)
if a==b:
    print(True)
if a!=b:
    print(True)   
    
# python IS keyword
x = 10
y = 10

if x is y:
    print(True)
else:
    print(False)
x = ["a", "b", "c", "d"]
y = ["a", "b", "c", "d"] 

print(x is y)

# python in operator
# Python program to demonstrate 
# in keyword 

# Create a list 
animals = ["dog", "lion", "cat"] 

# Check if lion in list or not 
if "lion" in animals: 
	print(True)


         
                 
         
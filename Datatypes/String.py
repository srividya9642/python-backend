# strings
# strings are sequence of characters ,strings are immutable data type it means once we created a string we cannot modified.
# by creating a string we used single quotes(''),double quotes (""),or triple quotes(''' ''') and also we can use triple quotes with allows multiple lines.


# creating a string
# by using single quotes
string1 = 'welcome'
print("string by using single quotes")
print(string1)


#by using double quotes
string2 = "hello! there"
print("\nstring by using double quotes")
print(string2)

#by using triple quotes
string3 = ''' Hello Good morning !'''
print("\nstring by using triple quotes")
print(string3)

# quotes allows multiple lines
string4 = '''Good
              Morning
              friends'''
print("\n creating a multiline string:")
print(string4)       






# python string positive indexing
string1 = "Hello good morning"
print ("Initial string: ",string1)

#printing first character
print("first character of string is :",string1[0])       



# python string negative indexing
string2 = "Hello good morning"
print ("Initial string: ",string2)

#printing last character
print("last character of string is :",string2[-1])



#string slicing
# creating a slice
string_1 = "goodnight"
print("Initial string :")
print(string_1)
# printing 3rd to 8th character
print("\n Slicing the character from 3 to 8 :")
print(string_1[3:8])


# printing caracters between
# 3rd and 2nd last character
print("\n Slicing characters between"+
    "3rd and 2nd last characters:")
print(string_1[3:-2])



# string reversed by using string slicing method:
gm = "goodmorning"
print(gm[::-1])
# string reversed by using  built-in join and reversed
gm = "goodmorning"
# reverse the string using reversed and join function
gm = "".join(reversed(gm))
 
print(gm)

 #reverse string using slice method'''
string = "srividyabellamkonda"
print(string[::-1])

''' reverse the string using join and reversed function'''
string = "".join(reversed(string))
print(string)




# Deleting/Updating from a string
''' in python, the updation and deletion of characters from a string is not allowed.this will cause an error because item assignment or item deletion from a string
is not supported.Although deletion of the entire string is possible with the help of built-in "del" keyword.This is because strings are immutable.hence elements of 
a strings cannot be changed once assigned.only new strings can be reassigned to the same name.'''

# Updating a character
''' A character of a string can be updated in python by converting the string into python list
and then updating the element in the list.As list are "mutable" in nature,we can update the character and then convert the list back into the string.'''
                       
string1 = "Hello Good morning"
print("Initial string:")
print(string1)
# updating a character of the string
# 1st way
list1 = list(string1)
list1[2] = 'p'
string2 = ''.join(list1)
print("\n updating character at 2nd Index :")
print(string2)


# by using string slicing method
# 2nd way
string3 = string1[0:2] + 'p'+ string1[3:]


# updating entire string

string1 ="hello good morning"
print("Initial string:")
print(string1)

# updating a string
string1 = "hello world"
print("\n updated string :")
print(string1)
 
 
 # Deleting a character from string
string1 = "hello good morning"
print("Initial string:")
print(string1)

print("Deleting character at 2nd index:")
del string1[2]
print(string1)

# by using slicing we can remove the character from the original string
#  And strore the result in a new string.

string1 = "Hello Good Morning"
print("Initial string:")
print(string1)

# Deleting A character
string2 = string1[0:2]+ string1[3:]
print("\n deleting character at 2nd index:")
print(string2)

# Deleting whole string by using "del" keyword

string1 = "Hello Good Morning"
print("Initial string:")
print(string1)

# deleting entire string  with the use of "del"
del string1
print("\n deleting entire string:")
print(string1)

# Escspe sequencing in python
# Initial string 
Name_1 = '''I'm a "geek" '''
print("Initial string with use of triple quotes:")
print(Name_1)

# Escaping single quotes
Name_2 = 'I\'m a "Geek"'
print("\n Escaping single quotes:")
print(Name_2)

# Escaping double quotes
Name_3 = "I\'m a \"Geek\""
print("\n Escaping double quotes")
print(Name_3)

# printing paths with the 
# use of Escape sequence
Name_4 = "Hi\tGeeks"
print("\nTab:")
print(Name_4)



# python string formatting
''' strings in python or string data type in python can be formatted with the use of "format()."
method which is a very versatile and powerful tool for formatting strings.format method in string 
contains curly braces{} as placehlders which can hold arguments according to position or keyword to specify the order.'''

# python program for
# formatting of strigs

# default order
string_f = "{} {} {}".format('Geeks','for','Life')
print("print string in default order: ")
print(string_f)

# positional formatting
string_f = "{1} {0} {2}".format('Geeks', 'for','life')
print("\nprint string in positional arguments: ")
print(string_f)

# keyword formatting
string_f = "{l} {f} {g}".format(g='Geeks', f='For', l='life')
print("\nprint string in order of keyword: ")
print(string_f)
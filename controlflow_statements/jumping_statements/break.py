# the "break" statement we cam stop the loop before it has looped through all the items:
'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "cherry":
      break'''


 # exit the loop when x is "banana" , but this time the break comes before thye print:
fruits = ["apple", "banana", "cherry"]  
for x in fruits:
     if x == "banana":
         break 
     print(x)        
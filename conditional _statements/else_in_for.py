# the else keyword in forloop specifies a block of code to be executed when he loop is finished:
'''for x in range(6):
    print(x)
else:
    print("Finally Finished")'''
    
    
# NOTE: the else block will not be executed if the loop is stopped by a break statement.
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally Finished!")    
        
        
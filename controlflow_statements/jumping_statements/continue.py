# with the continue statement we can stop the current iteration of the loop,and continue with the next:
fruits = ["grapes", "mango", "jackfruit"]
for x in fruits:
    if x == "mango":
        continue
    print(x)
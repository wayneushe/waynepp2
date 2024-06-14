#for loops
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)

#jumping through an item inside a loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
     continue
  print(x)  

#range function to loop through a code set 6 times 
for x in range(6):
   print(x)

#how to exit a loop a when a certain condition is met
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
     break
  print(x)   



#sets{remove and discard work the same }
"""There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates."""

#checking if an element is present in a set
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
   print("Yes, apple is a fruit!")


#to add an element to a set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#adding multiple elements to a set
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#to remove items from a set
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#removing items using discard 
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


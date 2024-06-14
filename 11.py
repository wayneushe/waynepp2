#dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
"""thisdict = {

}
print(thisdict[blah])"""

#using the get mothod to obtain a certain key
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#changing the value for a certain key
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020

#adding a key to the dictionary
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"

#removing items using pop
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop('model')

#using clear to empty a dictionary
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()



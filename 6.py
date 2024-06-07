#lenth of a string 
x="Hello World"
print(len(x))

#get the first character of the string txt
txt="Hello World"
x=txt[0]

#get characters from index 2 to index 4(llo)
txt="Hello World"
txt=txt[2:5]

#return string without any whitespace at the beginning or the end
txt="  Hello World  "
x=txt.strip()

#convert the value of txt to upper case 
txt="Hello World"
txt=txt.upper()

#convert to lower case
txt="Hello World"
txt=txt.lower()

#Replace H with J 
txt="Hello World!"
txt=txt.replace("H","J")

#insert the correct syntax to add a placeholder for the age parameter 
age=36
txt="My name is John, and i am {}"
print(txt.format(age))
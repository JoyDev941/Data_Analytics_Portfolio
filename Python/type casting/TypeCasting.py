#this is tutorial for converting numbers
#to check type for a variable element is type()

intnum = 100
floatnum = float(intnum)
strnum = str(floatnum)

print("This number is a float")
print(floatnum)
print("This number is a integer")
print(intnum)
print("This is a string")
print(type(strnum))


#What if

text = "Hello!"
#print(int(text)) # not allowed because the letters cannot become a number

text2 = "100"
print("you can convert a text with numbers to a integer or a float")
print(int(text2))

#what happens when you convert a float to integer
num = 99.9
print("you can convert the number from float to int, but it will remove the decimal part")
print(int(num))

#convert a literal string (just a string written by developer) to a integer or float

text = '123.25'
#print(int(text)) # you cant do this one
print("you can print only the correct format. int will be converted only if the literal string is an actual integer. otherwise, in our case the answer will be outputed in float")
print(float(text))
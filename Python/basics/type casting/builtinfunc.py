text = "hello"
alist = ["h", "e", "l", "l", "o"]

#len function

print("you can use the len function to check the length of a list or a litteral string")
print(len(text))
print(type(text))
print(len(alist))
print(type(alist))

#bin function
print("you can virtually convert integers into its binary equivalent")
num = 123
numf = 123.234
print(bin(num))
#print(bin(numf)) you cant do for string either only int


#oct and hex, simply converts octal and hexagonal representation

#round simply rounds up a number
print("rounded 123.234")
print(round(numf))

#id returns the memory address location of the variable
print("Memory address of numf")
print(id(numf))

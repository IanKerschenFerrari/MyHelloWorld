myStr = "Hello Worldz"
print("My name is " + myStr)
print(f"My name is {myStr}")
print("My name is {0}".format(myStr))

print(dir(mystr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello', 'bye').upper())
print(myStr.count('l'))

print(myStr.startswith('Hello'))
print(myStr.endswith('World'))

print(myStr.split('o'))
print(myStr.find('o'))

print(len(myStr))
print(myStr.index('e'))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])
print(myStr[-1])
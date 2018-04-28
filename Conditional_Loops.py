

#if-elif-else

message = "hi"

if message == 'hi':
	print("hi")
elif message == 'hey':
	print("hey")
else:
	print("messgae not received")

#print address of the string

print(id(message))

"""
False statement is going to be returned in following cases:

1. count = 0,,,numerical datatype has a 0 value
2. empty ''()[]{}
3. var = False
4. None
"""


meg = None

if meg:
	print("hey")
else:
	print("not")

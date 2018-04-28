

employee = {'name':'Cheryl', 'age': 23, 'qualification': 'MBBS'}

print(employee)

print(employee['name'])               #....to print value for a specific key

#......to print value for a key, which doesn't exist

#print(employee['phone']) ...this will give a key error,
# and the program will halt, better way to deal with it is to use get() method 

print(employee.get('phone'))      #..........this will print None, by default
print(employee.get('phone', "default value"))  #this will set the value which is given in the second argument

#to add values to the dictionary

employee['salary'] = 200000   #add new field
employee['age'] = 19          #updated value

print(employee) 

#another way to insert/update is to use update method

employee.update({'name':'Joey', 'gender':'M'})

print(employee)

del employee['gender']

print(employee)

popped = employee.pop('salary')
print(popped)
print(len(employee))               #provides number of keys

print(employee.keys())
print(employee.values())
print(employee.items())






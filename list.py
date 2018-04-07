

fruits = ['mango', 'orange', 'banana', 'kiwi', 'apple']

#print(fruits[x0],fruits[-1])
count = 1
#fruits.append('grapes')
#print(help(list))
fruits.insert(2,'grapes')

print(fruits)

fruits.remove('grapes')

print(fruits)

for x in xrange(0,len(fruits)):

	if fruits[x] == 'grapes':
							count = 0
							print(fruits[x])

#	else:
#		print("Grapes is not in the list")   

if count == 1:
			 print("Grapes is not present in the list")


vegetables = ['tomato', 'onion']

fruits.extend(vegetables)  #extend adds this new list to original list as individual elements
print(fruits)
fruits.append(vegetables)  #append/insert add new list as sub-list to the main list
print(fruits)
fruits.insert(-1,vegetables)
print(fruits[4:])

fruits.reverse() #reverse the orginal string, this will modify the original string
print(fruits)

fruits.sort()  #sort in ascending order the original string, this will modify the original string
print(fruits)

fruits.sort(reverse = True)  #sort in descending order the original string, this will modify the original string
print(fruits)

fruit_sorted_list = sorted(fruits)

print("using sorted function::",fruit_sorted_list)
#sorting method, which will not modify the orginal string

element = fruit_sorted_list.pop(5)
print element

print(fruit_sorted_list.index('orange'))

for fruit in fruit_sorted_list:                      #iterate through the list
	print(fruit)


print("look here first")
for index,fruit in enumerate(fruit_sorted_list):
	print(index,fruit)

print("look here")
for index,fruit in enumerate(fruit_sorted_list, start = 2):    #this will start the index for the list from 2
	print(index,fruit)


#convert list into string

new_list = ['lambo', 'model s', 'range rover', 'db9']

str_speed = ', '.join(new_list)                             #join doesn't work on nested lists
print(str_speed)


#convert string into list

new_list2 = str_speed.split(', ')

print(new_list2)


#way to define an empty list

new_list = []
#or
new_list = list()
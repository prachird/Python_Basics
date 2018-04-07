#tuple are immutable objects i.e. cannot be modified,add or remove once after the 
#assignment. 


tuple_new = ('cat', 'cow', 'goat', 'dog', 'hen')

print(tuple_new)


#empty tuple

tuple_new = ()


#or
tuple_new = tuple()

print(tuple_new)

#as tuples are immutable, operations like insert, remove, reverse cannot be performed 
#on tuples


tuple_2 = tuple_new

print(tuple_2)

tuple_2[0] = 'rat'                           #immutability


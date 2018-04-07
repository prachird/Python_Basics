
set_singers = {'harry', 'niall', 'taylor', 'justin', 'selena', 'one republic', 'miley', 'camileo'}
#order of insertion is not maintained in sets

print(set_singers)

set_male_singers = {'justin', 'harry', 'weekend', 'niall', 'zayn', 'louie'}

print(set_male_singers)


#union
print(set_singers.union(set_male_singers))

#intersection
print(set_singers.intersection(set_male_singers))

#difference
print(set_male_singers.difference(set_singers))

print(set_singers.difference(set_male_singers))


#empty set

set_new = set()
print(set_new)


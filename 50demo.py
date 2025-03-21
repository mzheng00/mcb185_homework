# set is a mutable container, all elements unique and not ordered
# every time you run, it is different order
s = {'A', 'C', 'G'}
print(s)

# add items to set, adding the same items doesn't do anything
# no order so can't pick an iteration
s.add('T')
print(s)

# dictionary has strings instead of number indices
# there is no append()
d = {}
d = dict()

d = {'dog': 'woof', 'cat' : 'meow'}
print(d)

# access items in dictionary
print(d['cat'])

# add new items
d['pig'] = 'oink'
print(d)

# change value of item, access with its key
d['cat'] = 'mew'
print(d)

# delete an item using del
del d['cat']
print(d)

# check if key exists use in
if 'dog' in d:
    print(d['dog'])

# iterate through dictionary
for key in d:
    print(f'{key} says {d[key]}')

# most common way to iterate through dictionary is dict.items()
for k, v in d.items():
    print(k, 'says', v)

# just the keys or just the values
print(d.keys(), d.values(), list(d.values()))